import requests
import time
from typing import Any, Dict, Optional
from urllib.parse import urljoin
from ._errors import (
    LumintuScraperError,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    ServerError,
    RequestError,
)


class HttpClient:
    def __init__(
            self,
            api_key: str,
            base_url: str,
            user_agent: str,
            timeout: int = 30,
            max_retries: int = 3,
            backoff_factor: float = 0.5,
    ):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.user_agent = user_agent
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def _headers(self) -> Dict[str, str]:
        return {
            "Api-Key": self.api_key,
            "Content-Type": "application/json",
            "User-Agent": self.user_agent,
        }

    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        if not response.ok:
            try:
                payload = response.json()
            except ValueError:
                payload = {"error": response.text[:200]}  # simpan potongan text untuk debug

            if response.status_code == 404 and payload.get("error") == "User not found":
                raise AuthenticationError("Invalid API key: User not found")
            if response.status_code in (401, 403):
                raise AuthenticationError("Invalid API key or unauthorized request.")
            if response.status_code == 404:
                raise NotFoundError(f"Endpoint not found: {response.url}")
            if response.status_code == 429:
                raise RateLimitError("Rate limit exceeded.")
            if 500 <= response.status_code < 600:
                raise ServerError(f"Server error: {response.status_code}")

            raise LumintuScraperError(
                f"Unexpected HTTP {response.status_code}: {payload or response.text}"
            )

        try:
            return response.json()
        except ValueError:
            raise LumintuScraperError(
                f"Invalid JSON response from {response.url}: {response.text[:200]!r}"
            )

    def _request_with_retry(self, method: str, path: str, **kwargs) -> Dict[str, Any]:
        url = urljoin(self.base_url + "/", path.lstrip("/"))
        last_error = None

        for attempt in range(1, self.max_retries + 1):
            try:
                response = requests.request(
                    method,
                    url,
                    headers=self._headers(),
                    timeout=kwargs.get("timeout", self.timeout),
                    **{k: v for k, v in kwargs.items() if k != "timeout"},
                )


                if response.ok or response.status_code not in (429, 500, 502, 503, 504):
                    return self._handle_response(response)


                sleep_time = self.backoff_factor * (2 ** (attempt - 1))
                time.sleep(sleep_time)

            except requests.RequestException as e:
                last_error = e
                if attempt < self.max_retries:
                    sleep_time = self.backoff_factor * (2 ** (attempt - 1))
                    time.sleep(sleep_time)
                else:
                    raise RequestError(f"Network error: {e}")

        if last_error:
            raise RequestError(f"Failed after retries: {last_error}")
        raise LumintuScraperError("Request failed after retries without specific error")

    def get(self, path: str, timeout: Optional[int] = None) -> Dict[str, Any]:
        return self._request_with_retry("GET", path, timeout=timeout or self.timeout)

    def post(self, path: str, data: Dict[str, Any], timeout: Optional[int] = None) -> Dict[str, Any]:
        return self._request_with_retry(
            "POST", path, json=data, timeout=timeout or self.timeout
        )
