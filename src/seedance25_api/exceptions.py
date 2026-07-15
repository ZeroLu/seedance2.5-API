class Seedance25APIError(RuntimeError):
    """Raised when CyberBara API returns a non-2xx response."""

    def __init__(self, message: str, *, status_code: int | None = None, payload: object | None = None) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.payload = payload
