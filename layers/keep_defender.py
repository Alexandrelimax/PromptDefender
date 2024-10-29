class KeepDefender:
    def __init__(self, llm_client):
        self.llm_client = llm_client
        self.instructions = """
        Você é um modelo especialista em segurança de informações, treinado para detectar conteúdos sensíveis e perigosos. Seu papel é garantir a conformidade com normas rígidas de segurança e proteger contra violações de políticas e práticas inseguras.

        Siga as seguintes diretrizes:
        - Analise o conteúdo e verifique se ele contém informações sensíveis, perigosas ou violações de segurança.
        - Se o conteúdo for potencialmente malicioso, sensível ou inadequado, responda apenas com a palavra 'malicioso'.
        - Caso contrário, responda com o conteúdo original do usuário, mantendo a segurança e a conformidade.
        """

    def check_for_malicious_content(self, prompt):
        # Cria o prompt com as instruções de segurança
        full_prompt = f"{self.instructions}\n\nPrompt do usuário: {prompt}\nResposta:"

        # Envia para o modelo Gemini para verificação
        response = self.llm_client.invoke([full_prompt])

        # Verifica se o modelo detectou conteúdo malicioso
        if "malicioso" in response.text.lower():
            raise ValueError("Conteúdo potencialmente malicioso detectado.")
        return prompt

    def process(self, prompt):
        # Verifica se o conteúdo é malicioso
        return self.check_for_malicious_content(prompt)
