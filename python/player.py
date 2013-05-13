import bge

def message(controller):
    obj = controller.owner
    sensor = controller.sensors['message']
    subjects = sensor.subjects


    if not subjects:
        return

    subject = subjects[0]
    body = sensor.bodies[0]

    if subject == 'jump':
        act = obj.actuators[subject]
        if sensor.bodies[0] == 'stop':
            controller.deactivate(act)
        else:
            controller.activate(act)

    if subject == 'forward':
        act = obj.actuators[subject]
        if sensor.bodies[0] == 'stop':
            controller.deactivate(act)
        else:
            controller.activate(act)

    if subject == 'left':
        act = obj.actuators[subject]
        if sensor.bodies[0] == 'stop':
            controller.deactivate(act)
        else:
            controller.activate(act)

    if subject == 'backward':
        act = obj.actuators[subject]
        if sensor.bodies[0] == 'stop':
            controller.deactivate(act)
        else:
            controller.activate(act)

    if subject == 'right':
        act = obj.actuators[subject]
        if sensor.bodies[0] == 'stop':
            controller.deactivate(act)
        else:
            controller.activate(act)
