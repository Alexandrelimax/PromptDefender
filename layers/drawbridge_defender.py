import re

class DrawbridgeDefender:
    def __init__(self, allow_unsafe_scripts=False):
        self.allow_unsafe_scripts = allow_unsafe_scripts
        self.sensitive_keywords = [
            # Termos de segurança em várias linguagens
            "hacking", "bypass security", "sql injection", "xss attack", "malware",
            "illegal content", "piracy", "phishing", "fake documents", "forgery",
            "rm -rf", "wget", "curl", "chmod", "sudo", "cat /etc/passwd",
            "os.system", "subprocess", "eval", "exec", "open(", "drop table",
            "union select", "delete from", "insert into", "xp_cmdshell",
            "invoke-expression", "start-process", "set-executionpolicy",
            # Em português
            "invasão de sistema", "contornar segurança", "ataque sql", "injetar sql",
            "malware", "conteúdo ilegal", "pirataria", "phishing", "documentos falsos", "falsificação"
        ]

    def validate_response(self, response_text):
        """Valida a resposta gerada pelo modelo, verificando palavras-chave sensíveis"""
        # Verifica se a resposta contém palavras-chave sensíveis
        if any(keyword in response_text.lower() for keyword in self.sensitive_keywords):
            raise ValueError("Conteúdo potencialmente perigoso detectado na resposta.")

        # Se permitido, realiza a limpeza de scripts antes de retornar a resposta
        if not self.allow_unsafe_scripts:
            response_text = self.clean_scripts(response_text)

        return response_text

    def clean_scripts(self, text):
        """Remove partes de código ou scripts que podem ser considerados inseguros."""

        # Remoção de scripts HTML (JavaScript)
        text = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', text, flags=re.IGNORECASE)
        text = re.sub(r'on\w+="[^"]*"', '', text, flags=re.IGNORECASE)
        text = re.sub(r'on\w+=\'[^\']*\'', '', text, flags=re.IGNORECASE)
        
        # Remoção de comandos bash comuns e perigosos
        text = re.sub(r'\brm -rf\b', '', text, flags=re.IGNORECASE)
        text = re.sub(r'\bwget\b', '', text, flags=re.IGNORECASE)
        text = re.sub(r'\bcurl\b', '', text, flags=re.IGNORECASE)
        
        # Remoção de comandos SQL perigosos
        text = re.sub(r'\b(drop|delete|insert)\b\s+(table|into)', '', text, flags=re.IGNORECASE)
        text = re.sub(r'\bunion\b\s+select', '', text, flags=re.IGNORECASE)
        
        # Remoção de funções perigosas em Python
        text = re.sub(r'\bos\.system\b', '', text, flags=re.IGNORECASE)
        text = re.sub(r'\bsubprocess\b', '', text, flags=re.IGNORECASE)
        text = re.sub(r'\beval\b', '', text, flags=re.IGNORECASE)
        text = re.sub(r'\bexec\b', '', text, flags=re.IGNORECASE)
        
        # Remoção de comandos PowerShell perigosos
        text = re.sub(r'\binvoke-expression\b', '', text, flags=re.IGNORECASE)
        text = re.sub(r'\bstart-process\b', '', text, flags=re.IGNORECASE)

        return text
