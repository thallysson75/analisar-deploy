def cadastrar_usuario(usuarios, nome, email):
    """Adiciona um usuário à lista."""
    nome = nome.strip()
    email = email.strip().lower()

    if len(nome) < 2:
        raise ValueError("O nome deve ter pelo menos 2 caracteres.")

    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError("Informe um e-mail válido.")

    if any(usuario["email"] == email for usuario in usuarios):
        raise ValueError("Este e-mail já está cadastrado.")

    usuario = {"nome": nome, "email": email}
    usuarios.append(usuario)
    return usuario


def listar_usuarios(usuarios):
    """Retorna todos os usuários cadastrados."""
    return usuarios.copy()


def buscar_usuario(usuarios, nome):
    """Busca um usuário pelo nome, sem diferenciar maiúsculas."""
    nome = nome.strip().lower()
    for usuario in usuarios:
        if usuario["nome"].lower() == nome:
            return usuario
    return None


def excluir_usuario(usuarios, email):
    """Exclui um usuário pelo e-mail. Retorna True se encontrar."""
    email = email.strip().lower()
    for usuario in usuarios:
        if usuario["email"] == email:
            usuarios.remove(usuario)
            return True
    return False
