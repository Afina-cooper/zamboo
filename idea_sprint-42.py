# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: IdeaSprint
import sys

def color_enabled():
    return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()

def color(text, fg=None, bg=None, bold=False, dim=False, underline=False, reverse=False):
    codes = []
    if bold: codes.append('1')
    if dim: codes.append('2')
    if underline: codes.append('4')
    if reverse: codes.append('7')
    if fg is not None: codes.append(f'3{fg}')
    if bg is not None: codes.append(f'4{bg}')
    reset = '\033[0m'
    if color_enabled():
        return f'\033[{";".join(codes)}m{text}{reset}'
    return text

class IdeaSprintColors:
    HEADER = color('IdeaSprint', fg=35, bold=True)
    IDEA = color('{idea}', fg=35, bold=True)
    TASK = color('{task}', fg=33, bold=True)
    HYPOTHESIS = color('{hypothesis}', fg=36, bold=True)
    RESULT = color('{result}', fg=32, bold=True)
    STATUS_DONE = color('{status}', fg=32)
    STATUS_PENDING = color('{status}', fg=33)
    STATUS_FAILED = color('{status}', fg=31)
    COMMENT = color('{comment}', fg=37)
    ERROR = color('{error}', fg=31, bold=True)
    INFO = color('{info}', fg=36)
    SUBTITLE = color('{subtitle}', fg=37, bold=True)
    SEPARATOR = color('-' * 60, fg=37)
