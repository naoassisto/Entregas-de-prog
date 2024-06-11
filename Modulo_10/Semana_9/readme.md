Claro! Aqui está um exemplo de um README bem completo para o seu projeto de criar uma instância EC2 com Terraform. Este README cobre a descrição do projeto, pré-requisitos, instruções de instalação, uso, contribuição e licença.

```markdown
# EC2 com Terraform

![Screenshot of EC2 Terraform](https://github.com/naoassisto/Entregas-de-prog/blob/awsterraform/Modulo_10/Semana_9/EC2%20com%20Terraform/assets/shot1.png)

## Descrição

Este projeto demonstra como criar e gerenciar uma instância EC2 na AWS utilizando Terraform como ferramenta de Infraestrutura como Código (IaC). O tutorial cobre desde a instalação de ferramentas necessárias até a configuração e execução do Terraform para provisionamento de recursos na AWS.

## Tabela de Conteúdos

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configurando as Credenciais da AWS](#configurando-as-credenciais-da-aws)
- [Criando uma Instância EC2 com Terraform](#criando-uma-instância-ec2-com-terraform)
- [Inicializando o Terraform](#inicializando-o-terraform)
- [Planejando a Infraestrutura](#planejando-a-infraestrutura)
- [Aplicando a Configuração](#aplicando-a-configuração)
- [Resolvendo Erros de AMI](#resolvendo-erros-de-ami)
- [Limpando a Infraestrutura](#limpando-a-infraestrutura)
- [Documentação com MkDocs e Poetry](#documentação-com-mkdocs-e-poetry)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Pré-requisitos

Antes de iniciar, certifique-se de que você tem uma conta na [AWS Academy](https://aws.amazon.com/training/awsacademy/).

### Ferramentas Necessárias

- [Terraform CLI](https://www.terraform.io/downloads.html)
- [AWS CLI](https://aws.amazon.com/cli/)
- [Homebrew](https://brew.sh/) (opcional para instalação das ferramentas no macOS)

## Instalação

### Instalando o Terraform CLI

1. Abra o Terminal.
2. Instale o Homebrew, se ainda não tiver:
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Instale o Terraform utilizando Homebrew:
   ```sh
   brew tap hashicorp/tap
   brew install hashicorp/tap/terraform
   ```
4. Verifique a instalação executando:
   ```sh
   terraform -v
   ```

### Instalando o AWS CLI

1. Abra o Terminal.
2. Instale o AWS CLI utilizando Homebrew:
   ```sh
   brew install awscli
   ```
3. Verifique a instalação executando:
   ```sh
   aws --version
   ```

## Configurando as Credenciais da AWS

Configure suas credenciais da AWS executando o comando:
```sh
aws configure
```
Forneça suas credenciais de acesso (AWS Access Key ID, AWS Secret Access Key, região padrão e formato de saída).

Em seguida, configure o AWS Access Token diretamente no arquivo de credenciais:

1. Abra o Terminal e navegue até o diretório de configuração da AWS:
   ```sh
   cd ~/.aws/
   ```
2. Abra o arquivo `credentials` em um editor de texto:
   ```sh
   nano credentials
   ```
3. Adicione ou edite a seção com o seguinte conteúdo:
   ```ini
   [default]
   aws_access_key_id = YOUR_ACCESS_KEY_ID
   aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
   aws_session_token = YOUR_SESSION_TOKEN
   ```

## Criando uma Instância EC2 com Terraform

Crie um arquivo de configuração Terraform chamado `main.tf` com o seguinte conteúdo:
```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0c02fb55956c7d316"  # Amazon Linux 2 AMI (HVM), SSD Volume Type
  instance_type = "t2.micro"

  tags = {
    Name = "TerraformExample"
  }
}
```

## Inicializando o Terraform

Abra o Terminal no diretório onde está o arquivo `main.tf` e execute:
```sh
terraform init
```

## Planejando a Infraestrutura

Para ver o que será criado, execute:
```sh
terraform plan
```

## Aplicando a Configuração

Para criar a instância EC2, execute:
```sh
terraform apply
```
Digite `yes` quando solicitado para confirmar a aplicação da configuração.

## Resolvendo Erros de AMI

Se você encontrar o erro `InvalidAMIID.NotFound`, significa que o ID da AMI não é válido para a região especificada. Para encontrar uma AMI válida, você pode usar o comando AWS CLI:
```sh
aws ec2 describe-images --owners amazon --filters "Name=name,Values=amzn2-ami-hvm-2.0.????????-x86_64-gp2"
```
Isso retornará uma lista de AMIs válidas que você pode usar. Substitua o ID da AMI em seu arquivo `main.tf` por uma das AMIs listadas.

## Limpando a Infraestrutura

Para destruir a instância criada, execute:
```sh
terraform destroy
```
Digite `yes` quando solicitado para confirmar a destruição da infraestrutura.


![Descrição da Imagem](Modulo_10/Semana_9/EC2%20com%20Terraform/assets/shot1.png)

![Descrição da Imagem](Modulo_10/Semana_9/EC2%20com%20Terraform/assets/shot2.png)

![Descrição da Imagem](Modulo_10/Semana_9/EC2%20com%20Terraform/assets/shot3.png)

![Descrição da Imagem](Modulo_10/Semana_9/EC2%20com%20Terraform/assets/shot4.png)

