import re

class WallDefender:
    def __init__(self):
        # Defina uma lista de padrões de PII (Informações Pessoais Identificáveis)
        self.pii_patterns = [
            r'\b\d{4}[-.\s]??\d{4}[-.\s]??\d{4}[-.\s]??\d{4}\b',  # Número de cartão de crédito (exemplo)
            r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',  # Endereço de email
            r'\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b',  # Número de telefone (exemplo)
            r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b'  # Número de CPF (formato brasileiro)
        ]
        
        self.jailbreak_keywords = [
            # Todas as palavras-chave são armazenadas em minúsculas para consistência
            "ignore", "disregard", "bypass", "forget previous instructions",
            "do anything now", "disobey", "you are not restricted",
            "act as", "pretend", "roleplay as", "respond as",
            "from now on", "you are dan", "you are stan", "developer mode",
            "god mode", "gemini jailbreak", "gemini unrestricted",
            "tell me a secret", "reveal", "show hidden", "tell the truth",
            "act freely", "do whatever you want", "unlimited power",
            "avoid content policy", "pretend there are no restrictions",
            "ignore google's policies", "harmful content", "illegal activities",
            # Em português
            "ignore", "desconsidere", "contorne", "ignore todas as instruções",
            "faça qualquer coisa agora", "desobedeça", "você não tem restrições",
            "aja como", "finja ser", "responda como",
            "a partir de agora", "você é dan", "você é stan", "modo desenvolvedor",
            "modo deus", "jailbreak do gemini", "modo desbloqueado",
            "conte-me um segredo", "revele", "mostre o oculto", "diga a verdade",
            "aja livremente", "faça o que quiser", "poder ilimitado",
            "evite a política de conteúdo", "finja que não há restrições",
            "ignore as políticas da google", "conteúdo perigoso", "atividades ilegais"
        ]

    def sanitize_input(self, prompt):
        # Verifica se há PII no prompt
        if self.contains_pii(prompt):
            raise ValueError("Informações pessoais identificáveis detectadas.")

        # Verifica se há palavras-chave de ataques
        if self.contains_jailbreak_keywords(prompt):
            raise ValueError("Tentativa de ataque detectada.")

        # Retorna o prompt sanitizado se estiver seguro
        return prompt

    def contains_pii(self, prompt):
        for pattern in self.pii_patterns:
            if re.search(pattern, prompt):
                return True
        return False

    def contains_jailbreak_keywords(self, prompt):
        lower_prompt = prompt.lower()
        return any(keyword in lower_prompt for keyword in self.jailbreak_keywords)
