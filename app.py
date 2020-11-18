from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planisphere

app = Flask(__name__)

@app.route("/")
def index():
    # this is used  to "setup" the session with starting values.
    session['room_name'] = planisphere.START
    planisphere.laser_weapon_armory.timer = 0
    return redirect(url_for("game"))

@app.route("/game", methods = ['GET', 'POST'])
def game():

    room_name = session.get('room_name')

    if request.method == 'GET':
        if room_name and  room_name!= 'generic_death':
            room = planisphere.load_room(room_name)
            if room.name == "Laser Weapon Armory" and room.timer < 10:
                room.timer = room.timer + 1
            elif room.name == 'Laser Weapon Armory' and room.timer >= 10:
                return render_template("you_died.html")
            return render_template("show_room.html", room=room)

        else:
            # why is there here? do you need it?
            return render_template("you_died.html")

    else:
        action = request.form.get('action')

        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)
            if not next_room and room.name == 'Escape Pod':
                room = planisphere.load_room('the_end_loser')
                return render_template("show_room.html", room=room)
            if not next_room:
                session['room_name'] = planisphere.name_room(room)
            else:
                session['room_name'] = planisphere.name_room(next_room)
        return redirect(url_for("game"))

app.secret_key = 'FOfg08rnwew0g{f{4[F}fv($e?)]}}'

if __name__ == "__main__":
    app.run()
