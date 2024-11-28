def format_responses(responses: list[dict]) -> list[dict]:
    if responses is not None:
        for response in responses:
            response.comment = response.comentario
            response.comentario = response.comentario.replace("\n", "<br>")
        return responses