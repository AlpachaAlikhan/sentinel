from dataclasses import dataclass, field


#Finding описывает найденную проблему
@dataclass
class Finding:
    title: str
    severity: str
    description: str


#ScanResult описывает результат проверки одного порта
@dataclass
class ScanResult:
    target: str
    port: int
    state: str
    service: str | None = None
    version: str | None = None
    findings: list[Finding] = field(default_factory=list)