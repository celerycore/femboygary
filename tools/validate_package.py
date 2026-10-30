"""Validate built archive structure, decode sprites, and resolve AIR references."""
from pathlib import Path
import io,re,struct
from PIL import Image
root=Path(__file__).resolve().parents[1]
c=root/'chars/femboygary'
data=(c/'femboygary.sff').read_bytes()
assert data[:12]==b'ElecbyteSpr\0'
groups,count,offset,subsize=struct.unpack_from('<IIII',data,16)
assert subsize==32
seen=set(); offsets=set()
for i in range(count):
    assert offset not in offsets and offset>=512
    offsets.add(offset)
    nxt,length,x,y,g,n,previous,pal=struct.unpack_from('<IIhhHHHB',data,offset)
    blob=data[offset+32:offset+32+length]
    assert len(blob)==length and blob[0]==10
    im=Image.open(io.BytesIO(blob)); im.load()
    assert im.mode=='P'
    assert (g,n) not in seen
    seen.add((g,n))
    assert nxt==(offset+32+length if i+1<count else 0)
    offset=nxt
assert offset==0 and len(seen)==38
text=(c/'femboygary.air').read_text()
actions=set(map(int,re.findall(r'\[Begin Action (\d+)\]',text,re.I)))
refs=0
for line in text.splitlines():
    m=re.match(r'^(-?\d+),(-?\d+),',line)
    if m:
        assert tuple(map(int,m.groups())) in seen,line
        refs+=1
for line in (c/'femboygary.cns').read_text().splitlines():
    m=re.match(r'\s*(?:anim|projanim|projhitanim|projremanim)\s*=\s*(\d+)\s*$',line)
    if m: assert int(m[1]) in actions,line
for name in ['femboygary.cmd','femboygary.cns','femboygary.air','femboygary.sff']:
    assert (c/name).is_file()
print(f'PASS: {len(seen)} PCX sprites decoded; {len(actions)} actions; {refs} AIR sprite references resolved.')
print('Engine load and combat checks remain unrun.')
