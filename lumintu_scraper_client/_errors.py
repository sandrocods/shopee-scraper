class LumintuScraperError(Exception):
    """Base error for LumintuScraperClient."""


class AuthenticationError(LumintuScraperError):
    """Raised when API key is invalid or unauthorized."""


class NotFoundError(LumintuScraperError):
    """Raised when resource is not found (404)."""


class RateLimitError(LumintuScraperError):
    """Raised when rate limit is exceeded (429)."""


class ServerError(LumintuScraperError):
    """Raised when server returns 5xx error."""


class RequestError(LumintuScraperError):
    """Raised for network/connection errors."""
