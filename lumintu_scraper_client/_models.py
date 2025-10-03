from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional


@dataclass
class UserInfo:
    concurrency_limit: int
    credits: int
    package: str
    subscription_start: datetime
    subscription_end: datetime
    total_requests_today: int

    @classmethod
    def from_dict(cls, data: dict) -> "UserInfo":
        return cls(
            concurrency_limit=data["concurrency_limit"],
            credits=data["credits"],
            package=data["package"],
            subscription_start=datetime.fromisoformat(data["subscription_start"]),
            subscription_end=datetime.fromisoformat(data["subscription_end"]),
            total_requests_today=data["total_requests_today"],
        )


@dataclass
class ScrapingResult:
    """
    Representasi hasil scraping dari API Lumintu Scraper.
    Bisa dibuat dari dict JSON hasil response API.
    Contoh:
        result = ScrapingResult.from_dict(api_response_dict)
    Atau bisa juga langsung akses atributnya:
        print(result.status)
        print(result.result)  # hasil scraping sebenarnya
    --------------------------------------------------------------
    Fields:
    - request_id: str
    - status: str (pending, running, success, failed)
    - status_code: int (HTTP-like status code)
    - message: str (pesan tambahan, terutama kalau gagal)
    - created_at: datetime (waktu request dibuat)
    - updated_at: Optional[datetime] (waktu terakhir status diupdate)
    - elapsed_time: Optional[float] (waktu proses dalam detik, kalau sudah selesai)
    - request_data: Dict[str, Any] (data input request)
    - result: Dict[str, Any] (hasil scraping sebenarnya)
    - timestamp: datetime (waktu response diterima)
    --------------------------------------------------------------
    """
    request_id: str
    status: str
    status_code: int
    message: str
    created_at: datetime
    updated_at: Optional[datetime]
    elapsed_time: Optional[float]
    request_data: Dict[str, Any]
    result: Dict[str, Any]
    timestamp: datetime

    @classmethod
    def from_dict(cls, data: dict) -> "ScrapingResult":
        return cls(
            request_id=data["request_id"],
            status=data["status"],
            status_code=data["status_code"],
            message=data.get("message", ""),
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]) if data.get("updated_at") else None,
            elapsed_time=data.get("elapsed_time"),
            request_data=data.get("request_data", {}),
            result=data.get("result", {}),
            timestamp=datetime.fromisoformat(data["timestamp"]),
        )
