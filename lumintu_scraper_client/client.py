import time
from typing import Any, Dict, Optional

from ._http_client import HttpClient
from ._logging import get_logger
from ._models import UserInfo, ScrapingResult
from ._errors import LumintuScraperError

logger = get_logger()


class LumintuScraperClient:
    def __init__(
            self,
            api_key: str,
            base_url: str = "https://lumintuscraper.com",
            user_agent: Optional[str] = None,
            timeout: int = 30,
            max_retries: int = 3,
            backoff_factor: float = 0.5,
    ):
        self.http = HttpClient(
            api_key=api_key,
            base_url=base_url,
            user_agent=user_agent or "LumintuScraperClient/0.1.0",
            timeout=timeout,
            max_retries=max_retries,
            backoff_factor=backoff_factor,
        )

    def actor(self, actor_path: str):
        return ActorCall(self.http, actor_path)


    def user(self):
        return UserClient(self.http)

    def result(self):
        return ResultClient(self.http)


class ActorCall:
    def __init__(self, http: HttpClient, actor_path: str):
        self.http = http
        self.actor_path = f"api/{actor_path.strip('/')}"

    def call(self, inputs: Optional[Dict[str, Any]] = None, timeout: int = 60) -> Dict[str, Any]:
        logger.info(f"Calling actor: {self.actor_path}")
        return self.http.post(self.actor_path, inputs or {}, timeout=timeout)


class UserClient:
    def __init__(self, http: HttpClient):
        self.http = http

    def info(self, timeout: int = 30, as_dict: bool = False) -> UserInfo:
        logger.info("Fetching user info")
        response = self.http.get("api/user/info", timeout=timeout)

        if not response.get("status") or "data" not in response:
            raise RuntimeError("Failed to fetch user info")

        return response if as_dict else UserInfo.from_dict(response["data"])


class ResultClient:
    def __init__(self, http: HttpClient):
        self.http = http

    def get(self, request_id: str, timeout: int = 30, as_dict: bool = False):
        payload = {"request_id": request_id}
        response = self.http.post("scrape/result", data=payload, timeout=timeout)
        return response if as_dict else ScrapingResult.from_dict(response)

    def wait_for_result(
            self,
            request: Any,
            interval: int = 2,
            max_attempts: int = 30,
            timeout: int = 30,
            as_dict: bool = False,
    ):
        if isinstance(request, str):
            request_id = request
        elif isinstance(request, dict):
            request_id = request.get("request_id")
            if not request_id:
                raise LumintuScraperError("Response dict tidak mengandung 'request_id'")
        else:
            raise LumintuScraperError(
                f"Unsupported type for wait_for_result: {type(request)}"
            )

        for attempt in range(1, max_attempts + 1):
            logger.info(f"Checking result (attempt {attempt}/{max_attempts}) for {request_id}")
            result = self.get(request_id, timeout=timeout, as_dict=True)
            if result.get("status") in ("completed", "failed", "success"):
                return result if as_dict else ScrapingResult.from_dict(result)

            time.sleep(interval)

        raise TimeoutError(
            f"Result not ready after {max_attempts} attempts (interval {interval}s)"
        )
