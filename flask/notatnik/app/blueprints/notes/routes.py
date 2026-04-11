from flask import jsonify, request, abort, render_template
from . import notes_bp
from app.models import db, Note


@notes_bp.route("/", methods=["GET"])
def get_notes():
    notes = Note.query.all()
    return render_template("notes/index.html", notes=notes)
    # return jsonify({"notes": [n.to_dict() for n in notes]})


@notes_bp.route("/", methods=["POST"])
def create_note():
    data = request.get_json()
    if not data or "title" not in data or "content" not in data:
        abort(400, "Wymagane pola: title, content")

    note = Note(title=data["title"], content=data["content"])
    db.session.add(note)
    db.session.commit()
    return jsonify(note.to_dict()), 201


@notes_bp.route("/<int:note_id>", methods=["GET"])
def get_note(note_id):
    note = db.get_or_404(Note, note_id)
    return jsonify(note.to_dict())