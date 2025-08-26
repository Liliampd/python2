from flask import render_template, request, redirect, url_for, flash, abort
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
# agora importamos também create_user e user_exists
from app.alquimias import validate_user_password, create_user, user_exists
from app.models.models import Post

# HOME: lista posts do mais novo para o mais antigo
@app.route("/")
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    user = current_user if current_user.is_authenticated else None
    return render_template("index.html", user=user, posts=posts)

# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        remember = bool(request.form.get("remember"))
        user = validate_user_password(username, password)
        if user:
            login_user(user, remember=remember)
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for("index"))
        else:
            flash("Usuário ou senha inválidos.", "error")
    return render_template("login.html")

# LOGOUT
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Você saiu da sua conta.", "info")
    return redirect(url_for("index"))

# PERFIL (exemplo de rota protegida)
@app.route("/perfil")
@login_required
def perfil():
    return f"Área protegida. Usuário: {current_user.username}"

# REGISTRO (novo) — cria conta e já autentica
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = (request.form.get("username") or "").strip()
        password = (request.form.get("password") or "")
        confirm  = (request.form.get("confirm") or "")

        # validações simples
        if not username or not password:
            flash("Preencha usuário e senha.", "error")
            return render_template("register.html")
        if len(password) < 6:
            flash("A senha deve ter pelo menos 6 caracteres.", "error")
            return render_template("register.html")
        if password != confirm:
            flash("As senhas não conferem.", "error")
            return render_template("register.html")
        if user_exists(username):
            flash("Este usuário já existe. Tente outro.", "error")
            return render_template("register.html")

        # criar e logar
        u = create_user(username, password)
        login_user(u)
        flash("Conta criada! Você já está logada.", "success")
        return redirect(url_for("index"))

    return render_template("register.html")

# CRIAR POST
@app.route("/post/novo", methods=["GET", "POST"])
@login_required
def novo_post():
    if request.method == "POST":
        body = (request.form.get("body") or "").strip()
        if not body:
            flash("Escreva algo antes de publicar.", "error")
            return render_template("new_post.html")
        post = Post(body=body, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Post publicado!", "success")
        return redirect(url_for("index"))
    return render_template("new_post.html")

# EDITAR POST
@app.route("/post/<int:post_id>/editar", methods=["GET", "POST"])
@login_required
def editar_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user_id != current_user.id:
        abort(403)
    if request.method == "POST":
        body = (request.form.get("body") or "").strip()
        if not body:
            flash("O post não pode ficar vazio.", "error")
            return render_template("edit_post.html", post=post)
        post.body = body
        db.session.commit()
        flash("Post atualizado!", "success")
        return redirect(url_for("index"))
    return render_template("edit_post.html", post=post)

# EXCLUIR POST
@app.route("/post/<int:post_id>/excluir", methods=["POST"])
@login_required
def excluir_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user_id != current_user.id:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Post excluído!", "info")
    return redirect(url_for("index"))
