#!/usr/bin/env python3
"""Check published documentation. Does not read or change any installed VM."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'guestinfo.svga.wddm.vsyncDefaultHz': '120',
    'guestinfo.svga.wddm.vsyncMaxHz': '120',
    'guestinfo.svga.wddm.vsyncThread': 'TRUE',
    'mks.lowCompositingFPS': '120',
    'mks.maxCompositingFPS': '120',
}
errors = []
snippet = (ROOT / 'examples/120hz.vmx.txt').read_text()
expected = ''.join(f'{key} = "{value}"\n' for key, value in EXPECTED.items())
if snippet != expected:
    errors.append('The snippet differs from the five tested settings.')
readme = (ROOT / 'README.md').read_text()
if f'```ini\n{snippet}```' not in readme:
    errors.append('README configuration and example snippet differ.')

for path in ROOT.rglob('*'):
    if '.git' in path.relative_to(ROOT).parts or not path.is_file():
        continue
    if path.suffix.lower() in {'.vmx', '.vmdk', '.vmem', '.vmss', '.vmsn', '.nvram', '.log', '.bak'}:
        errors.append(f'Private VM artifact must not be published: {path.relative_to(ROOT)}')
    if path.suffix != '.md':
        continue
    content = path.read_text()
    if content.count('```') % 2:
        errors.append(f'Unclosed code fence: {path.relative_to(ROOT)}')
    if re.search(r'/Users/[^/\s]+/|C:\\Users\\', content):
        errors.append(f'Personal filesystem path: {path.relative_to(ROOT)}')
    for target in re.findall(r'\]\(([^)\s]+)\)', content):
        if target.startswith(('https://', 'http://', '#', 'mailto:')):
            continue
        local = unquote(target.split('#', 1)[0])
        if local and not (path.parent / local).exists():
            errors.append(f'Broken local link in {path.relative_to(ROOT)}: {target}')

if errors:
    print('\n'.join(errors), file=sys.stderr)
    raise SystemExit(1)
print('PASS: exact five-line snippet, README consistency, local file links, code fences, and artifact/path checks.')
print('Scope: external URLs, rendered layout, anchor targets, and VM behavior require separate review.')
