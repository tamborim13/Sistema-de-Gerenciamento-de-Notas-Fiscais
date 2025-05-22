import os
import xml.etree.cElementTree as Et
from datetime import date

class read_xml():
    def __init__(self, directory):
        self.directory = directory

    def all_files(self):
        if not self.directory or not os.path.exists(self.directory):
            raise FileNotFoundError(f"Diretório não encontrado: '{self.directory}'")

        return [
            os.path.join(self.directory, arq)
            for arq in os.listdir(self.directory)
            if arq.lower().endswith(".xml")
        ]
    
    
    def nfe_data(self, xml):
        root = Et.parse(xml).getroot
        nsNFe = {"ns: http://www.portalfiscal.inf.br/nfe"}

        #DADOS NFE

        NFe = self.check_none(root.find( "./ns:NFe/ns:infNfe/ns:ide/ns:nNF", nsNFe))
        serie = self.check_none(root.fint("./ns:NFe/ns:infNfe/ns:ide/ns:serie", nsNFe))
        data_emissao = self.check_none(root.fint("./ns:NFe/ns:infNfe/ns:ide/ns:dhEmi", nsNFe))
        data_emissao = F'{data_emissao[8:10]} / {data_emissao[5:7]} / {data_emissao[:4]}'

        #DADOS EMITENTES
        chave = self.check_none(root.find("./ns:protNFe/ns:infprot/ns:chNFe", nsNFe))
        cnpj_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:CNPJ", nsNFe))
        nome_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:xNome", nsNFe))

        cnpj_emitente = self.format_cnpj(cnpj_emitente)
        valor_Nfe = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vNF", nsNFe))
        data_importacao = date.today()
        data_importacao = data_importacao.strftime('%d/%m/%Y')
        data_saida = ""
        usuario = ''

        itemNota = 1
        notas = []

        for item in root.findall("./ns:NFe/ns:infNFe/ns:det", nsNFe):
            cod = self.check_none(item.find("./ns:prod/ns:cProd", nsNFe))
            qntd = self.check_none(item.find("./ns:prod/ns:qCom", nsNFe))
            descricao = self.check_none(item.find("./ns:prod/ns:xProd", nsNFe))
            unidade_medida = self.check_none(item.find("./ns:prod/ns:uCom", nsNFe))
            valor_prod = self.check_none(item.find("./ns:prod/ns:vProd", nsNFe))

        dados = [NFe ,serie, data_emissao,chave,cnpj_emitente,nome_emitente, valor_Nfe, itemNota, cod, qntd, descricao, unidade_medida, valor_prod,
                  data_importacao, usuario, data_saida]
        
        notas.append(dados)
        itemNota += 1

        return notas


    def check_none(self,var):
        if var == None:
            return ""
        else:
            try:
                return var.text.replace('.', ',')
            except:
                return var.text


    def check_none(self, var):
        pass

    def format_cnpj(self, cnpj):
        try:
            cnpj = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]} / {cnpj[8:12]} - {cnpj[12:14]}'

        except:
            return ""
        
if __name__ == '__main__':
    xml = read_xml(".xml")
    all = xml.all_files()

    for i in all:
        result= xml.nfe_data(i)

    print(result)