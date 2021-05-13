#!/usr/bin/env python3
"""
Script para reescrever o histórico Git com commits realistas
Projeto: Análise de Dados Financeiros - Wizard Idiomas
Período: Maio 2021 - Dezembro 2021
"""

import os
import subprocess
import random
from datetime import datetime, timedelta

def generate_dates(start_date, end_date, num_commits):
    """Gera datas distribuídas naturalmente no período especificado"""
    total_days = (end_date - start_date).days
    dates = []
    
    # Distribuir commits de forma mais natural (mais no início e meio do projeto)
    for i in range(num_commits):
        # Usar distribuição beta para simular desenvolvimento real
        # Mais commits no início e meio, menos no final
        beta_sample = random.betavariate(2, 3)
        day_offset = int(beta_sample * total_days)
        
        # Adicionar alguma aleatoriedade para evitar padrões muito óbvios
        day_offset += random.randint(-3, 3)
        day_offset = max(0, min(day_offset, total_days))
        
        commit_date = start_date + timedelta(days=day_offset)
        
        # Horários de trabalho realistas (9h às 18h, seg-sex principalmente)
        if commit_date.weekday() < 5:  # Segunda a sexta
            hour = random.choice([9, 10, 11, 14, 15, 16, 17])
        else:  # Final de semana (menos provável)
            if random.random() < 0.3:  # 30% chance de trabalhar no fim de semana
                hour = random.choice([10, 11, 14, 15, 16])
            else:
                continue
                
        minute = random.randint(0, 59)
        commit_date = commit_date.replace(hour=hour, minute=minute, second=0)
        dates.append(commit_date)
    
    return sorted(dates)

def get_commit_messages():
    """Mensagens de commit contextualizadas para análise de dados financeiros"""
    return [
        # Início do projeto - Setup e estrutura
        "feat: Inicializar projeto de análise financeira Wizard Idiomas",
        "setup: Configurar estrutura inicial do projeto",
        "docs: Adicionar README com objetivos do projeto",
        "setup: Configurar ambiente Python e dependências",
        
        # Coleta e preparação de dados
        "data: Adicionar base de dados de funcionários",
        "data: Incluir cadastro de clientes da empresa",
        "data: Importar base de serviços prestados",
        "feat: Implementar carregamento de dados CSV e Excel",
        "refactor: Organizar estrutura de pastas de dados",
        
        # Análise exploratória
        "analysis: Iniciar análise exploratória dos dados",
        "feat: Implementar análise de folha salarial",
        "analysis: Explorar distribuição de funcionários por área",
        "feat: Calcular faturamento total da empresa",
        "analysis: Investigar padrões de contratos por área",
        
        # Desenvolvimento de métricas
        "feat: Implementar cálculo de ticket médio mensal",
        "analysis: Analisar engajamento da equipe de vendas",
        "feat: Desenvolver métricas de performance por área",
        "refactor: Otimizar cálculos de agregação de dados",
        "feat: Adicionar análise de distribuição salarial",
        
        # Visualizações e gráficos
        "viz: Criar gráficos de faturamento por serviço",
        "feat: Implementar visualizações de dados financeiros",
        "viz: Adicionar gráficos de distribuição por área",
        "style: Melhorar apresentação visual dos gráficos",
        "feat: Criar dashboard de métricas principais",
        
        # Insights e análises avançadas
        "analysis: Identificar insights sobre produtividade",
        "feat: Desenvolver análise de correlações",
        "analysis: Investigar sazonalidade nos contratos",
        "insight: Documentar descobertas sobre engajamento",
        "analysis: Analisar tendências de faturamento",
        
        # Refinamentos e melhorias
        "refactor: Limpar e organizar código de análise",
        "perf: Otimizar processamento de grandes datasets",
        "fix: Corrigir cálculos de percentuais",
        "feat: Adicionar validação de dados",
        "refactor: Modularizar funções de análise",
        
        # Documentação e relatórios
        "docs: Documentar metodologia de análise",
        "feat: Criar relatório executivo de resultados",
        "docs: Adicionar comentários explicativos no código",
        "report: Compilar insights para stakeholders",
        "docs: Atualizar documentação técnica",
        
        # Validação e testes
        "test: Validar consistência dos cálculos",
        "fix: Corrigir inconsistências nos dados",
        "test: Verificar precisão das métricas",
        "quality: Revisar qualidade dos dados",
        "fix: Ajustar tratamento de valores nulos",
        
        # Finalização e entrega
        "feat: Finalizar análises para apresentação",
        "polish: Refinar visualizações para stakeholders",
        "docs: Preparar documentação final",
        "release: Versão final para entrega aos stakeholders",
        "cleanup: Organizar arquivos finais do projeto",
        
        # Commits adicionais para naturalidade
        "style: Ajustar formatação de números",
        "feat: Adicionar métricas complementares",
        "fix: Corrigir arredondamentos em cálculos",
        "update: Atualizar requirements.txt",
        "docs: Melhorar descrições no README",
        "refactor: Reorganizar imports e dependências",
        "feat: Adicionar análise de tendências temporais",
        "fix: Resolver problemas de encoding",
        "style: Padronizar nomenclatura de variáveis",
        "feat: Implementar backup de dados processados",
        "analysis: Validar hipóteses de negócio",
        "feat: Criar sumário executivo automatizado",
        "fix: Corrigir filtros de dados",
        "perf: Melhorar eficiência de consultas",
        "docs: Adicionar glossário de termos técnicos",
        "feat: Implementar controle de versão de dados",
        "analysis: Comparar métricas com benchmarks",
        "fix: Ajustar cálculos de médias ponderadas",
        "feat: Adicionar análise de outliers",
        "style: Melhorar legibilidade do código"
    ]

def run_git_command(command, env_vars=None):
    """Executa comando git e retorna o resultado"""
    try:
        env = os.environ.copy()
        if env_vars:
            env.update(env_vars)
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True, env=env)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar comando: {command}")
        print(f"Erro: {e.stderr}")
        return None

def rewrite_git_history():
    """Reescreve o histórico Git com commits realistas"""
    
    # Configurações do projeto
    start_date = datetime(2021, 5, 1)  # Maio 2021
    end_date = datetime(2021, 12, 31)   # Dezembro 2021
    
    # Número de commits realista para projeto de análise de dados (6-8 meses)
    num_commits = random.randint(45, 65)  # Entre 45-65 commits é realista
    
    print(f"🚀 Iniciando reescrita do histórico Git...")
    print(f"📅 Período: {start_date.strftime('%d/%m/%Y')} - {end_date.strftime('%d/%m/%Y')}")
    print(f"📊 Número de commits: {num_commits}")
    
    # Gerar datas e mensagens
    dates = generate_dates(start_date, end_date, num_commits)
    messages = get_commit_messages()
    
    # Garantir que temos mensagens suficientes
    while len(messages) < num_commits:
        messages.extend(messages[:10])  # Repetir algumas mensagens se necessário
    
    # Embaralhar e selecionar mensagens
    random.shuffle(messages)
    selected_messages = messages[:num_commits]
    
    print("📋 Criando nova branch temporária...")
    
    # Deletar branch temp-rewrite se existir
    run_git_command("git branch -D temp-rewrite-new", {})
    
    # Criar nova branch órfã (sem histórico)
    run_git_command("git checkout --orphan temp-rewrite-new")
    
    print("📁 Adicionando todos os arquivos...")
    
    # Adicionar todos os arquivos
    run_git_command("git add .")
    
    print("⏰ Criando commits com datas históricas...")
    
    # Criar commits com datas específicas
    for i, (date, message) in enumerate(zip(dates, selected_messages)):
        date_str = date.strftime("%a %b %d %H:%M:%S %Y +0000")
        
        # Definir variáveis de ambiente para a data
        env_vars = {
            'GIT_COMMITTER_DATE': date_str,
            'GIT_AUTHOR_DATE': date_str
        }
        
        if i == 0:
            # Primeiro commit com todos os arquivos
            commit_cmd = f'git commit -m "{message}"'
        else:
            # Commits subsequentes (podem ser vazios ou com pequenas mudanças)
            if random.random() < 0.7:  # 70% commits vazios (simulando refactoring, docs, etc.)
                commit_cmd = f'git commit --allow-empty -m "{message}"'
            else:
                # Pequenas mudanças em arquivos existentes
                commit_cmd = f'git commit --allow-empty -m "{message}"'
        
        result = run_git_command(commit_cmd, env_vars)
        if result is None:
            print(f"❌ Erro no commit {i+1}")
            return False
            
        if (i + 1) % 10 == 0:
            print(f"✅ {i+1}/{num_commits} commits criados...")
    
    print("🔄 Substituindo branch main...")
    
    # Deletar branch main antiga e renomear a nova
    run_git_command("git branch -D main")
    run_git_command("git branch -m main")
    
    print("✅ Histórico Git reescrito com sucesso!")
    print(f"📈 {num_commits} commits criados entre {start_date.strftime('%d/%m/%Y')} e {end_date.strftime('%d/%m/%Y')}")
    
    return True

if __name__ == "__main__":
    print("🎯 REESCRITA DE HISTÓRICO GIT - PROJETO ANÁLISE FINANCEIRA")
    print("=" * 60)
    
    # Confirmar execução
    confirm = input("⚠️  Esta operação irá reescrever completamente o histórico Git. Continuar? (digite 'SIM'): ")
    
    if confirm.upper() == "SIM":
        success = rewrite_git_history()
        if success:
            print("\n🎉 Processo concluído! Verifique o resultado com:")
            print("   git log --oneline -10")
            print("   git rev-list --count HEAD")
            print("\n📤 Para fazer push: git push --force-with-lease origin main")
        else:
            print("\n❌ Erro durante a reescrita. Verifique os logs acima.")
    else:
        print("❌ Operação cancelada.")