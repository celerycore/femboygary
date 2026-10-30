from pathlib import Path
C=Path(__file__).resolve().parents[1]/'chars/femboygary'
(C/'femboygary.def').write_text('''[Info]
name = "Femboy Gary"
displayname = "Femboy Gary"
versiondate = 10,30,2026
mugenversion = 1.0
author = "celerycore"
localcoord = 320,240
[Files]
cmd = femboygary.cmd
cns = femboygary.cns
st = femboygary.cns
stcommon = common1.cns
sprite = femboygary.sff
anim = femboygary.air
[Arcade]
intro.storyboard =
ending.storyboard =
''')
base='''[Data]
life = 1000
power = 3000
attack = 100
defence = 100
fall.defence_up = 50
liedown.time = 60
airjuggle = 15
sparkno = 2
guard.sparkno = 40
KO.echo = 0
volume = 0
IntPersistIndex = 60
FloatPersistIndex = 40
[Size]
xscale = .55
yscale = .55
ground.back = 42
ground.front = 48
air.back = 35
air.front = 40
height = 100
attack.dist = 100
proj.attack.dist = 90
proj.doscale = 1
head.pos = 25,-90
mid.pos = 0,-45
shadowoffset = 0
draw.offset = 0,0
[Velocity]
walk.fwd = 2.2
walk.back = -1.7
run.fwd = 5.5,0
run.back = -4,-3
jump.neu = 0,-8.5
jump.back = -2.8
jump.fwd = 3.2
runjump.back = -3,-8.5
runjump.fwd = 4.5,-8.5
airjump.neu = 0,-8
airjump.back = -3
airjump.fwd = 3
[Movement]
airjump.num = 1
airjump.height = 35
yaccel = .44
stand.friction = .82
crouch.friction = .82
stand.friction.threshold = .05
crouch.friction.threshold = .05
air.gethit.groundlevel = 25
air.gethit.groundrecover.ground.threshold = -20
air.gethit.groundrecover.groundlevel = 10
air.gethit.airrecover.threshold = -1
air.gethit.airrecover.yaccel = .35
air.gethit.trip.groundlevel = 15
down.bounce.offset = 0,20
down.bounce.yaccel = .4
down.bounce.groundlevel = 12
down.friction.threshold = .05
'''
states=[base]
def ctrl(s): states.append(s+'\n')
def attack(n,anim,kind,damage,start,end,total,vel=0,fall=0):
    typ='A' if kind=='A' else 'C' if kind=='C' else 'S'
    ctrl(f'''[Statedef {n}]
type = {typ}
movetype = A
physics = {typ}
anim = {anim}
ctrl = 0
poweradd = 25
[State {n}, movement]
type = VelSet
trigger1 = Time = 0
x = {vel}
[State {n}, hit]
type = HitDef
trigger1 = Time = {start}
attr = {typ}, NA
hitflag = MAF
 guardflag = {'L' if kind=='C' and n==420 else 'H' if kind=='A' else 'MA'}
animtype = {'Hard' if damage>=90 else 'Light'}
damage = {damage},0
pausetime = 7,7
sparkno = 2
sparkxy = 0,-45
ground.type = {'Trip' if fall else 'High'}
ground.slidetime = 12
ground.hittime = {18 if damage<90 else 24}
ground.velocity = -{3 if damage<90 else 5}, { -5 if fall else 0}
air.velocity = -3,-4
fall = {fall}
getpower = 35,10
givepower = 20,10
[State {n}, end]
type = ChangeState
trigger1 = AnimTime = 0
value = {50 if kind=='A' else 11 if kind=='C' else 0}
ctrl = 1
''')
for row,kind,nums in [(0,'S',[200,210,220]),(0,'C',[400,410,420]),(0,'A',[600,610,620])]:
    for i,n in enumerate(nums): attack(n,n,kind,[35,65,95][i],5,10,24,[0,.8,1.5][i],int(n==420))
# Short airborne burst, with one use per airtime.
ctrl('''[Statedef 110]
type = A
movetype = I
physics = N
anim = 110
ctrl = 0
[State 110, once]
type = VarSet
trigger1 = Time = 0
v = 0
value = 1
[State 110, velocity]
type = VelSet
trigger1 = Time = 0
x = ifelse(command = "holdback", -4.5, 6)
y = 0
[State 110, recover]
type = ChangeState
trigger1 = Time >= 14
value = 50
ctrl = 1
[Statedef 1000]
type = S
movetype = A
physics = S
anim = 1000
ctrl = 0
poweradd = 40
[State 1000, burst]
type = Projectile
trigger1 = Time = 10
projid = 1000
projanim = 1001
projhitanim = 1002
projremanim = 1002
projremove = 1
projremovetime = 45
projhits = 1
projpriority = 1
offset = 45,-40
velocity = 5,0
attr = S, SP
damage = 90,12
animtype = Medium
hitflag = MAF
guardflag = MA
pausetime = 0,9
sparkno = 2
sparkxy = 0,0
ground.type = High
ground.slidetime = 15
ground.hittime = 22
ground.velocity = -5
air.velocity = -3,-4
getpower = 50,15
givepower = 25,10
[State 1000, end]
type = ChangeState
trigger1 = AnimTime = 0
value = 0
ctrl = 1
''')
attack(1100,1100,'S',110,7,14,32,6,1)
ctrl('''[Statedef 1200]
type = S
movetype = I
physics = S
anim = 1200
ctrl = 0
[State 1200, shield]
type = HitOverride
trigger1 = Time < 12
attr = SCA, NA, SA, NP, SP
slot = 0
stateno = 1210
time = 1
[State 1200, recover]
type = ChangeState
trigger1 = Time >= 25
value = 0
ctrl = 1
''')
attack(1210,220,'S',85,2,9,25,2)
ctrl('''[Statedef 3000]
type = S
movetype = A
physics = S
anim = 3000
ctrl = 0
poweradd = -1000
[State 3000, freeze]
type = SuperPause
trigger1 = Time = 0
time = 25
movetime = 25
anim = -1
darken = 1
p2defmul = 1
[State 3000, text]
type = Explod
trigger1 = Time = 0
anim = 3010
ID = 3010
pos = 0,-80
postype = p1
bindtime = 1
removetime = -2
sprpriority = 5
ownpal = 1
[State 3000, launch]
type = VelSet
trigger1 = Time = 25
x = 10
[State 3000, strike]
type = HitDef
trigger1 = Time = 26
attr = S, HA
damage = 260,30
animtype = Hard
hitflag = MAF
guardflag = MA
pausetime = 12,14
sparkno = 3
ground.type = High
ground.slidetime = 25
ground.hittime = 30
ground.velocity = -7,-6
air.velocity = -7,-6
fall = 1
getpower = 0,0
givepower = 40,20
[State 3000, end]
type = ChangeState
trigger1 = AnimTime = 0
value = 0
ctrl = 1
[Statedef -2]
[State -2, reset air dash]
type = VarSet
trigger1 = StateType != A
v = 0
value = 0
''')
(C/'femboygary.cns').write_text('\n'.join(states))
commands='''[Remap]
x = x
y = y
z = z
a = a
b = b
c = c
s = s
[Defaults]
command.time = 15
command.buffer.time = 3
'''
for name,keys in [('super','D, F, D, F, z'),('text','D, DF, F, x'),('shell','D, DB, B, y'),('FF','F, F'),('BB','B, B'),('recovery','x+y')]+[(x,x) for x in ['x','y','z','a','s']]+[('holdfwd','/F'),('holdback','/B'),('holdup','/U'),('holddown','/D')]:
    commands+=f'\n[Command]\nname = "{name}"\ncommand = {keys}\ntime = {1 if keys.startswith("/") else 20}\n'
commands+='\n[Statedef -1]\n'
def change(name,n,conditions):
    global commands
    commands+=f'\n[State -1, {name}]\ntype = ChangeState\nvalue = {n}\ntriggerall = command = "{name}"\n'+conditions+'\n'
change('super',3000,'triggerall = power >= 1000\ntriggerall = StateType != A\ntrigger1 = ctrl\ntrigger2 = MoveContact && StateNo = [200,220]')
for name,n in [('text',1000),('shell',1100)]: change(name,n,'triggerall = StateType != A\ntrigger1 = ctrl\ntrigger2 = MoveContact && StateNo = [200,220]')
change('a',1200,'triggerall = StateType = S\ntrigger1 = ctrl')
for name,n in [('FF',110),('BB',110)]: change(name,n,'triggerall = StateType = A\ntriggerall = Var(0) = 0\ntrigger1 = ctrl')
for name,n in [('FF',100),('BB',105)]: change(name,n,'triggerall = StateType = S\ntrigger1 = ctrl')
for base,typ in [(600,'A'),(400,'C'),(200,'S')]:
    for i,name in enumerate(['x','y','z']):
        cond=f'triggerall = StateType = {typ}\ntrigger1 = ctrl'
        if i: cond+=f'\ntrigger2 = MoveContact && StateNo = {base+(i-1)*10}'
        change(name,base+i*10,cond)
(C/'femboygary.cmd').write_text(commands)
# Animation data: sprite frames are row,column; all axes are ground-aligned.
animations={}
def anim(n,frames,attack=False,loop=False,hurt=True): animations[n]=(frames,attack,loop,hurt)
def f(r,c,t=6): return (r,c,t)
for n in [0,5,6]: anim(n,[f(0,i,8) for i in range(3)],loop=True)
for n in [10,11,12]: anim(n,[f(1,0,-1 if n==11 else 4)])
for n in [20,21,100]: anim(n,[f(0,i,5) for i in range(3,6)],loop=True)
anim(105,[f(1,5,15)])
for n in [40,41,42]: anim(n,[f(1,1,3)])
for n in [43,44,45,50]: anim(n,[f(1,2,6),f(1,3,-1)])
for n in [46,47]: anim(n,[f(1,0,4)])
anim(110,[f(1,4,14)])
for n in [120,130,131,132,140,150,151,152]: anim(n,[f(1,0,-1)])
for n in [170,180,181,190,195]: anim(n,[f(4,5,12),f(0,0,12)],loop=True)
for n in [5000,5001,5002,5010,5011,5012,5020,5021,5022,5030,5035,5040,5050,5060,5070,5080]: anim(n,[f(4,0 if n<5010 else 1 if n<5020 else 2,12)])
for n in [5100,5160,5170,5110,5120,5140,5150,5200,5210]: anim(n,[f(4,4 if n==5120 else 3,8 if n==5120 else -1)])
for base,row in [(200,2),(400,2),(600,3)]:
    for i in range(3):
        frames=[f(2,0,5),f(2,1,4),f(2,2,10)] if i==0 else [f(2,3,6),f(2,4,5),f(2,5,13)] if i==1 else [f(3,0,8),f(3,1,6),f(3,2,17)]
        if base==600: frames=[f(3,3+i,5),f(3,3+i,5),f(1,3,10)]
        anim(base+i*10,frames,attack=True)
anim(1000,[f(2,0,10),f(2,1,5),f(2,2,18)])
anim(1001,[f(5,i,6) for i in range(3)],attack=True,loop=True,hurt=False)
anim(1002,[f(5,i,3) for i in range(3,6)],hurt=False)
anim(1100,[f(2,3,7),f(2,4,9),f(2,5,18)],attack=True)
anim(1200,[f(1,0,25)])
anim(3000,[f(3,0,26),f(3,1,16),f(3,2,22)],attack=True)
anim(3010,[f(5,i,5) for i in range(6)],hurt=False)
lines=['; Generated animation definitions; sprite axes 128,232.']
for n,(frames,attack,loop,hurt) in sorted(animations.items()):
    lines+=[f'\n[Begin Action {n}]']
    if hurt: lines+=['Clsn2Default: 1',' Clsn2[0] = -72,-172,78,0']
    for idx,(r,c,t) in enumerate(frames):
        if attack and (idx==1 or n==1001):
            lines+=['Clsn1: 1', ' Clsn1[0] = -105,-135,105,-20' if n==1001 else ' Clsn1[0] = 0,-150,125,-15']
        lines+=[f'{r},{c},0,0,{t}']
(C/'femboygary.air').write_text('\n'.join(lines)+'\n')
print('Wrote DEF, CMD, CNS and',len(animations),'AIR actions')
