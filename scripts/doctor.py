#!/usr/bin/env python3
"""Read-only environment check for the Windows-first training workflow."""

from __future__ import annotations

import platform
import shutil
import subprocess
from dataclasses import dataclass


@dataclass(frozen=True)
class Tool:
    name: str
    commands: tuple[str, ...]
    required_on_windows: bool = True


TOOLS = (
    Tool("Git", ("git",)),
    Tool("CMake", ("cmake",)),
    Tool("CTest", ("ctest",)),
    Tool("MSVC compiler", ("cl",)),
    Tool("Ninja", ("ninja",), required_on_windows=False),
    Tool("PowerShell", ("pwsh", "powershell"), required_on_windows=False),
    Tool("WSL2", ("wsl.exe", "wsl"), required_on_windows=False),
)


def first_available(commands: tuple[str, ...]) -> str | None:
    return next((path for command in commands if (path := shutil.which(command))), None)


def version_line(path: str) -> str:
    candidates = ([path, "--version"], [path, "/?"])
    for command in candidates:
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=5, check=False)
        except (OSError, subprocess.SubprocessError):
            continue
        output = (result.stdout or result.stderr).strip().splitlines()
        if output:
            return output[0][:160]
    return "版本信息不可用"


def main() -> int:
    is_windows = platform.system() == "Windows"
    print(f"平台：{platform.platform()}")
    missing_required: list[str] = []
    for tool in TOOLS:
        path = first_available(tool.commands)
        if path:
            print(f"[OK] {tool.name}: {path} | {version_line(path)}")
        else:
            requirement = "必需" if is_windows and tool.required_on_windows else "可选/当前平台不要求"
            print(f"[--] {tool.name}: 未找到（{requirement}）")
            if is_windows and tool.required_on_windows:
                missing_required.append(tool.name)

    if missing_required:
        print("缺少 Windows 必需工具：" + "、".join(missing_required))
        print("若只缺少 cl，请先在 Visual Studio Developer PowerShell 中重试。")
        return 1
    if not is_windows:
        print("当前不是 Windows：本次仅验证跨平台辅助工具，Windows 门禁仍需在目标机器完成。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
