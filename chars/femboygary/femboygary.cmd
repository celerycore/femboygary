[Remap]
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

[Command]
name = "super"
command = D, F, D, F, z
time = 20

[Command]
name = "text"
command = D, DF, F, x
time = 20

[Command]
name = "shell"
command = D, DB, B, y
time = 20

[Command]
name = "FF"
command = F, F
time = 20

[Command]
name = "BB"
command = B, B
time = 20

[Command]
name = "recovery"
command = x+y
time = 20

[Command]
name = "x"
command = x
time = 20

[Command]
name = "y"
command = y
time = 20

[Command]
name = "z"
command = z
time = 20

[Command]
name = "a"
command = a
time = 20

[Command]
name = "s"
command = s
time = 20

[Command]
name = "holdfwd"
command = /F
time = 1

[Command]
name = "holdback"
command = /B
time = 1

[Command]
name = "holdup"
command = /U
time = 1

[Command]
name = "holddown"
command = /D
time = 1

[Statedef -1]

[State -1, super]
type = ChangeState
value = 3000
triggerall = command = "super"
triggerall = power >= 1000
triggerall = StateType != A
trigger1 = ctrl
trigger2 = MoveContact && StateNo = [200,220]

[State -1, text]
type = ChangeState
value = 1000
triggerall = command = "text"
triggerall = StateType != A
trigger1 = ctrl
trigger2 = MoveContact && StateNo = [200,220]

[State -1, shell]
type = ChangeState
value = 1100
triggerall = command = "shell"
triggerall = StateType != A
trigger1 = ctrl
trigger2 = MoveContact && StateNo = [200,220]

[State -1, a]
type = ChangeState
value = 1200
triggerall = command = "a"
triggerall = StateType = S
trigger1 = ctrl

[State -1, FF]
type = ChangeState
value = 110
triggerall = command = "FF"
triggerall = StateType = A
triggerall = Var(0) = 0
trigger1 = ctrl

[State -1, BB]
type = ChangeState
value = 110
triggerall = command = "BB"
triggerall = StateType = A
triggerall = Var(0) = 0
trigger1 = ctrl

[State -1, FF]
type = ChangeState
value = 100
triggerall = command = "FF"
triggerall = StateType = S
trigger1 = ctrl

[State -1, BB]
type = ChangeState
value = 105
triggerall = command = "BB"
triggerall = StateType = S
trigger1 = ctrl

[State -1, x]
type = ChangeState
value = 600
triggerall = command = "x"
triggerall = StateType = A
trigger1 = ctrl

[State -1, y]
type = ChangeState
value = 610
triggerall = command = "y"
triggerall = StateType = A
trigger1 = ctrl
trigger2 = MoveContact && StateNo = 600

[State -1, z]
type = ChangeState
value = 620
triggerall = command = "z"
triggerall = StateType = A
trigger1 = ctrl
trigger2 = MoveContact && StateNo = 610

[State -1, x]
type = ChangeState
value = 400
triggerall = command = "x"
triggerall = StateType = C
trigger1 = ctrl

[State -1, y]
type = ChangeState
value = 410
triggerall = command = "y"
triggerall = StateType = C
trigger1 = ctrl
trigger2 = MoveContact && StateNo = 400

[State -1, z]
type = ChangeState
value = 420
triggerall = command = "z"
triggerall = StateType = C
trigger1 = ctrl
trigger2 = MoveContact && StateNo = 410

[State -1, x]
type = ChangeState
value = 200
triggerall = command = "x"
triggerall = StateType = S
trigger1 = ctrl

[State -1, y]
type = ChangeState
value = 210
triggerall = command = "y"
triggerall = StateType = S
trigger1 = ctrl
trigger2 = MoveContact && StateNo = 200

[State -1, z]
type = ChangeState
value = 220
triggerall = command = "z"
triggerall = StateType = S
trigger1 = ctrl
trigger2 = MoveContact && StateNo = 210
