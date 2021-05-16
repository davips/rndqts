#  Copyright (c) 2021. Davi Pereira dos Santos
#  This file is part of the rndqts project.
#  Please respect the license - more about this in the section (*) below.
#
#  rndqts is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  rndqts is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with rndqts.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is a crime and is unethical regarding the effort and
#  time spent here.
#  Relevant employers or funding agencies will be notified accordingly.
#
#  rndqts is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  rndqts is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with rndqts.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is a crime and is unethical regarding the effort and
#  time spent here.
#  Relevant employers or funding agencies will be notified accordingly.

# http://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm
# https://cdn.analyticafinance.com.br/courses/guia-de-tickers-da-b3/Guia-de-Tickers-da-B3.html#a%C3%A7%C3%B5es
import numpy as np
import pandas as pd


def b3() -> pd.DataFrame:
    txt = """class,ticker,naics,sector,subsector,segment,governance
          ON,QVQP3B,Empresa de eletricidade; gás e água,Financeiro,Outros,Outros,Balcão Organizado
          PN,ABCB4,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 2
          ON,EALT3,Transformação de aço em produtos de aço,Bens industriais,Máquinas e equipamentos,Máq. e equip. construção e agrícolas,Tradicional
          PN,EALT4,Transformação de aço em produtos de aço,Bens industriais,Máquinas e equipamentos,Máq. e equip. construção e agrícolas,Tradicional
          ON,ADHM3,Comércio atacadista de bens não duráveis variados,Saúde,Serviços médico-hospitalares análises e diagnósticos,Serviços médico-hospitalares análises e diagnósticos,Tradicional
          ON,TIET3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 2
          PN,TIET4,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 2
          UNT N2,TIET11,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 2
          ON,AFLT3,Empresa de eletricidade; gás e água,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          ON,ALEF3B,Administração de empresas e empreendimentos,Financeiro,Outros,Outros,Balcão Organizado
          ON,BRGE3,Administração de empresas e empreendimentos,Financeiro,Previdência e seguros,Bancos,Tradicional
          PNA,BRGE5,Administração de empresas e empreendimentos,Financeiro,Previdência e seguros,Bancos,Tradicional
          PNB,BRGE6,Administração de empresas e empreendimentos,Financeiro,Previdência e seguros,Bancos,Tradicional
          PNC,BRGE7,Administração de empresas e empreendimentos,Financeiro,Previdência e seguros,Bancos,Tradicional
          PND,BRGE8,Administração de empresas e empreendimentos,Financeiro,Previdência e seguros,Bancos,Tradicional
          PNE,BRGE11,Administração de empresas e empreendimentos,Financeiro,Previdência e seguros,Bancos,Tradicional
          PNF,BRGE12,Administração de empresas e empreendimentos,Financeiro,Previdência e seguros,Bancos,Tradicional
          ON,CRIV3,Bancos,Financeiro,Intermediários financeiros,Soc. crédito e financiamento,Tradicional
          PN,CRIV4,Bancos,Financeiro,Intermediários financeiros,Soc. crédito e financiamento,Tradicional
          ON,RPAD3,Administração de empresas e empreendimentos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          PNA,RPAD5,Administração de empresas e empreendimentos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          PNB,RPAD6,Administração de empresas e empreendimentos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          ON,BRIV3,Bancos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          PN,BRIV4,Bancos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          ON,ALSO3,Locadora de imóveis,Financeiro,Exploração de imóveis,Exploração de imóveis,Novo Mercado
          ON,APTI3,Indústria de molas e produtos de arame,Financeiro,Agropecuária,Holdings diversificadas,Tradicional
          PN,APTI4,Indústria de molas e produtos de arame,Financeiro,Agropecuária,Holdings diversificadas,Tradicional
          ON,FRRN3B,Transporte ferroviário,Bens industriais,Transporte,Transporte ferroviário,Balcão Organizado
          PNA,FRRN5B,Transporte ferroviário,Bens industriais,Transporte,Transporte ferroviário,Balcão Organizado
          PNB,FRRN6B,Transporte ferroviário,Bens industriais,Transporte,Transporte ferroviário,Balcão Organizado
          ON,AALR3,Laboratório de exames médicos,Saúde,Serviços médico-hospitalares análises e diagnósticos,Serviços médico-hospitalares análises e diagnósticos,Novo Mercado
          ON,ALPA3,Indústria de calçados,Consumo cíclico,Tecidos vestuário e calçados,Calçados,Nível 1
          PN,ALPA4,Indústria de calçados,Consumo cíclico,Tecidos vestuário e calçados,Calçados,Nível 1
          ON,APER3,Corretora de seguros,Financeiro,Previdência e seguros,Corretoras de seguros,Novo Mercado
          ON,ALUP3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 2
          PN,ALUP4,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 2
          UNT N2,ALUP11,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 2
          ON,BAZA3,Bancos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          ON,ABEV3,Indústria de bebidas,Consumo não cíclico,Bebidas,Cervejas e refrigerantes,Tradicional
          ON,CBEE3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          ON,ANIM3,Escola de ensino superior,Consumo cíclico,Diversos,Serviços educacionais,Novo Mercado
          ON,ARZZ3,Indústria de calçados,Consumo cíclico,Comércio,Tecidos vestuário e calçados,Novo Mercado
          ON,ATOM3,Telecomunicações,Financeiro,Outros,Outros,Tradicional
          ON,AZEV3,Outras construções pesadas e de engenharia civil,Bens industriais,Construção e engenharia,Construção pesada,Tradicional
          PN,AZEV4,Outras construções pesadas e de engenharia civil,Bens industriais,Construção e engenharia,Construção pesada,Tradicional
          PN,AZUL4,Transporte aéreo regular,Bens industriais,Transporte,Transporte aéreo,Nível 2
          ON,BTOW3,Vendas por correio ou meio eletrônico,Consumo cíclico,Comércio,Produtos diversos,Novo Mercado
          ON,B3SA3,Bolsa de valores e commodities,Financeiro,Serviços financeiros diversos,Serviços financeiros diversos,Novo Mercado
          ON,BAHI3,Administração de empresas e empreendimentos,Financeiro,Diversos,Holdings diversificadas,Bovespa Mais
          PN,BMGB4,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 1
          ON,BIDI3,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 2
          PN,BIDI4,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 2
          UNT,BIDI11,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 2
          PN,BPAN4,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 1
          ON,BGIP3,Bancos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          PN,BGIP4,Bancos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          ON,BEES3,Bancos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          PN,BEES4,Bancos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          ON,BPAR3,Bancos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          ON,BRSR3,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 1
          PNA,BRSR5,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 1
          PNB,BRSR6,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 1
          ON,BDLL3,Industria de máquinas agrícolas; de construção e mineração,Bens industriais,Máquinas e equipamentos,Máq. e equip. industriais,Tradicional
          PN,BDLL4,Industria de máquinas agrícolas; de construção e mineração,Bens industriais,Máquinas e equipamentos,Máq. e equip. industriais,Tradicional
          ON,BTTL3,Concessionárias de outros veículos motorizados,Financeiro,Comércio,Holdings diversificadas,Tradicional
          ON,BALM3,Indústria de equipamentos e materiais para uso médico,Saúde,Equipamentos,Equipamentos,Tradicional
          PN,BALM4,Indústria de equipamentos e materiais para uso médico,Saúde,Equipamentos,Equipamentos,Tradicional
          ON,BBML3,Transporte rodoviário,Bens industriais,Serviços diversos,Serviços diversos,Bovespa Mais
          ON,BBSE3,Seguradora,Financeiro,Previdência e seguros,Seguradoras,Novo Mercado
          ON,BETP3B,Atividades relacionadas à intermediação de crédito,Financeiro,Outros,Outros,Balcão Organizado
          ON,BMKS3,Indústria de outros equipamentos de transporte,Consumo cíclico,Viagens e lazer,Bicicletas,Tradicional
          ON,BIOM3,Pesquisa científica,Saúde,Medicamentos e outros produtos,Medicamentos e outros produtos,Bovespa Mais
          ON,BSEV3,Agricultura,Consumo não cíclico,Alimentos processados,Açúcar e álcool,Novo Mercado
          ON,GBIO33,Indústria de remédios,Saúde,Medicamentos e outros produtos,Medicamentos e outros produtos,BDR nível 3
          ON,BKBR3,Restaurantes e outros lugares para comer,Consumo cíclico,Hotéis e restaurantes,Restaurante e similares,Novo Mercado
          ON,BOBR3,Indústria de artigos de limpeza,Consumo não cíclico,Produtos de uso pessoal e de limpeza,Produtos de limpeza,Tradicional
          PN,BOBR4,Indústria de artigos de limpeza,Consumo não cíclico,Produtos de uso pessoal e de limpeza,Produtos de limpeza,Tradicional
          ON,BBRK3,Atividades relacionadas a imóveis,Financeiro,Exploração de imóveis,Intermediação imobiliária,Novo Mercado
          ON,BRML3,Locadora de imóveis,Financeiro,Exploração de imóveis,Exploração de imóveis,Novo Mercado
          ON,BRPR3,Locadora de imóveis,Financeiro,Exploração de imóveis,Exploração de imóveis,Novo Mercado
          ON,BBDC3,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 1
          PN,BBDC4,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 1
          ON,BRAP3,Administração de empresas e empreendimentos,Materiais básicos,Mineração,Minerais metálicos,Nível 1
          PN,BRAP4,Administração de empresas e empreendimentos,Materiais básicos,Mineração,Minerais metálicos,Nível 1
          ON,BBAS3,Bancos,Financeiro,Intermediários financeiros,Bancos,Novo Mercado
          ON,AGRO3,Agricultura,Consumo não cíclico,Agropecuária,Agricultura,Novo Mercado
          ON,BRKM3,Indústria química,Materiais básicos,Químicos,Petroquímicos,Nível 1
          PNA,BRKM5,Indústria química,Materiais básicos,Químicos,Petroquímicos,Nível 1
          PNB,BRKM6,Indústria química,Materiais básicos,Químicos,Petroquímicos,Nível 1
          ON,BSLI3,Bancos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          PN,BSLI4,Bancos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          ON,BRFS3,Abatedouros,Consumo não cíclico,Alimentos processados,Carnes e derivados,Novo Mercado
          ON,BRQB3,Editoras de software,Tecnologia da informação,Programas e serviços,Programas e serviços,Bovespa Mais
          ON,BPAC3,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 2
          PNA,BPAC5,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 2
          UNT,BPAC11,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 2
          ON,CABI3B,Administração de empresas e empreendimentos,Financeiro,Outros,Outros,Balcão Organizado
          ON,CACO3B,Administração de empresas e empreendimentos,Financeiro,Outros,Outros,Balcão Organizado
          ON,CAMB3,Indústria de calçados,Consumo cíclico,Tecidos vestuário e calçados,Calçados,Tradicional
          ON,CAML3,Outras indústrias de alimentos,Consumo não cíclico,Alimentos processados,Alimentos diversos,Novo Mercado
          ON,CPTP3B,Telecomunicações,Financeiro,Outros,Outros,Balcão Organizado
          ON,CRFB3,Loja de departamentos,Consumo não cíclico,Comércio e distribuição,Alimentos,Novo Mercado
          ON,CASN3,Água; esgoto e outros sistemas,Utilidade pública,Água e saneamento,Água e saneamento,Tradicional
          PN,CASN4,Água; esgoto e outros sistemas,Utilidade pública,Água e saneamento,Água e saneamento,Tradicional
          ON,CCRO3,Atividades auxiliares ao transporte rodoviário,Bens industriais,Transporte,Exploração de rodovias,Novo Mercado
          ON,CCXC3,Mineração de metais,Outros,Outros,Minerais não metálicos,Novo Mercado
          ON,CEAB3,Loja de roupas,Consumo cíclico,Comércio,Tecidos vestuário e calçados,Novo Mercado
          ON,CEBR3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          PNA,CEBR5,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          PNB,CEBR6,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          ON,CEDO3,Tecelagens,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Nível 1
          PN,CEDO4,Tecelagens,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Nível 1
          ON,CEED3,Empresa de eletricidade; gás e água,Utilidade pública,Energia elétrica,Energia elétrica,Nível 1
          PN,CEED4,Empresa de eletricidade; gás e água,Utilidade pública,Energia elétrica,Energia elétrica,Nível 1
          ON,EEEL3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 1
          PN,EEEL4,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 1
          ON,CEGR3,Distribuição de gás natural,Utilidade pública,Gás,Gás,Tradicional
          ON,CLSC3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 2
          PN,CLSC4,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 2
          ON,GPAR3,Empresa de eletricidade; gás e água,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          ON,CEPE3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          PNA,CEPE5,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          PNB,CEPE6,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          ON,RANI3,Indústria de papel; celulose e papelão,Materiais básicos,Madeira e papel,Papel e celulose,Tradicional
          PN,RANI4,Indústria de papel; celulose e papelão,Materiais básicos,Madeira e papel,Papel e celulose,Tradicional
          ON,MAPT3,Administração de empresas e empreendimentos,Financeiro,Outros,Outros,Tradicional
          PN,MAPT4,Administração de empresas e empreendimentos,Financeiro,Outros,Outros,Tradicional
          ON,CMIG3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 1
          PN,CMIG4,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 1
          ON,CNTO3,Loja de artigos esportivos e instrumentos musicais,Consumo cíclico,Comércio,Produtos diversos,Novo Mercado
          ON,CESP3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 1
          PNA,CESP5,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 1
          PNB,CESP6,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 1
          ON,HGTX3,Indústria de roupas de malha,Consumo cíclico,Tecidos vestuário e calçados,Vestuário,Novo Mercado
          ON,CIEL3,Serviços de processamento de dados; hospedagem e outros serviços relacionados,Financeiro,Serviços financeiros diversos,Serviços financeiros diversos,Novo Mercado
          ON,CMSA3,Administração de empresas e empreendimentos,Financeiro,Outros,Outros,Tradicional
          PN,CMSA4,Administração de empresas e empreendimentos,Financeiro,Outros,Outros,Tradicional
          ON,CNSY3,Indústria cinematográfica,Comunicações,Mídia,Produção e difusão de filmes e programas,Bovespa Mais
          ON,CEEB3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          PNA,CEEB5,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          PNB,CEEB6,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          ON,COCE3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          PNA,COCE5,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          PNB,COCE6,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          ON,COGN3,Escola de ensino superior,Consumo cíclico,Diversos,Serviços educacionais,Novo Mercado
          ON,CGAS3,Distribuição de gás natural,Utilidade pública,Gás,Gás,Tradicional
          PNA,CGAS5,Distribuição de gás natural,Utilidade pública,Gás,Gás,Tradicional
          ON,CRTE3B,Atividades auxiliares ao transporte rodoviário,Bens industriais,Transporte,Exploração de rodovias,Balcão Organizado
          PNA,CRTE5B,Atividades auxiliares ao transporte rodoviário,Bens industriais,Transporte,Exploração de rodovias,Balcão Organizado
          ON,CALI3,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Tradicional
          PN,CALI4,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Tradicional
          ON,CSMG3,Água; esgoto e outros sistemas,Utilidade pública,Água e saneamento,Água e saneamento,Novo Mercado
          ON,CPLE3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 1
          PNA,CPLE5,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 1
          PNB,CPLE6,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 1
          ON,CORR3,Administração de empresas e empreendimentos,Financeiro,Exploração de imóveis,Exploração de imóveis,Tradicional
          PN,CORR4,Administração de empresas e empreendimentos,Financeiro,Exploração de imóveis,Exploração de imóveis,Tradicional
          ON,CSAN3,Comércio atacadista de petróleo e produtos de petróleo,Petróleo gás e biocombustíveis,Petróleo gás e biocombustíveis,Exploração refino e distribuição,Novo Mercado
          ON,RLOG3,Transporte ferroviário,Bens industriais,Transporte,Transporte ferroviário,Novo Mercado
          ON,CSRN3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          PNA,CSRN5,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          PNB,CSRN6,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          ON,CTNM3,Indústria de roupas de tecido,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          PN,CTNM4,Indústria de roupas de tecido,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          ON,CPFE3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Novo Mercado
          ON,CPRE3,Empresa de eletricidade; gás e água,Utilidade pública,Energia elétrica,Energia elétrica,Novo Mercado
          ON,CRDE3,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Novo Mercado
          ON,CRPG3,Indústria química,Materiais básicos,Químicos,Químicos diversos,Tradicional
          PNA,CRPG5,Indústria química,Materiais básicos,Químicos,Químicos diversos,Tradicional
          PNB,CRPG6,Indústria química,Materiais básicos,Químicos,Químicos diversos,Tradicional
          ON,CARD3,Serviços de apoio a empresas,Bens industriais,Serviços diversos,Serviços diversos,Novo Mercado
          ON,CTCA3,Agricultura,Consumo não cíclico,Agropecuária,Agricultura,Bovespa Mais
          ON,CVCB3,Transporte turístico,Consumo cíclico,Viagens e lazer,Viagens e turismo,Novo Mercado
          ON,CCPR3,Locadora de imóveis,Financeiro,Exploração de imóveis,Exploração de imóveis,Novo Mercado
          ON,CYRE3,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Novo Mercado
          ON,DASA3,Laboratório de exames médicos,Saúde,Serviços médico-hospitalares análises e diagnósticos,Serviços médico-hospitalares análises e diagnósticos,Tradicional
          ON,PNVL3,Loja de artigos para saúde e cuidados pessoais,Saúde,Comércio e distribuição,Medicamentos e outros produtos,Tradicional
          PN,PNVL4,Loja de artigos para saúde e cuidados pessoais,Saúde,Comércio e distribuição,Medicamentos e outros produtos,Tradicional
          ON,DIRR3,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Novo Mercado
          ON,DOHL3,Indústria de roupas de tecido,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          PN,DOHL4,Indústria de roupas de tecido,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          ON,DMMO3,Extração de petróleo e gás,Petróleo gás e biocombustíveis,Petróleo gás e biocombustíveis,Exploração refino e distribuição,Tradicional
          ON,DTCY3,Outros tipos de escolas,Bens industriais,Serviços diversos,Serviços diversos,Tradicional
          PN,DTCY4,Outros tipos de escolas,Bens industriais,Serviços diversos,Serviços diversos,Tradicional
          ON,DTEX3,Indústria de móveis e afins,Materiais básicos,Madeira e papel,Madeira,Novo Mercado
          ON,ECOR3,Atividades auxiliares ao transporte rodoviário,Bens industriais,Transporte,Exploração de rodovias,Novo Mercado
          ON,ELEK3,Indústria química básica,Materiais básicos,Químicos,Petroquímicos,Tradicional
          PN,ELEK4,Indústria química básica,Materiais básicos,Químicos,Petroquímicos,Tradicional
          ON,EKTR3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          PN,EKTR4,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          ON,ELET3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 1
          PNA,ELET5,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 1
          PNB,ELET6,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 1
          ON,ETRO3B,Administração de empresas e empreendimentos,Financeiro,Outros,Outros,Balcão Organizado
          ON,LIPR3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          ON,EMAE3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          PN,EMAE4,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          ON,EMBR3,Indústria de equipamentos aeroespacias,Bens industriais,Material de transporte,Material aeronáutico e de defesa,Novo Mercado
          ON,ENAT3,Extração de petróleo e gás,Petróleo gás e biocombustíveis,Petróleo gás e biocombustíveis,Exploração refino e distribuição,Novo Mercado
          ON,ECPR3,Indústria de fios,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          PN,ECPR4,Indústria de fios,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          ON,ENBR3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Novo Mercado
          ON,ENGI3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 2
          PN,ENGI4,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 2
          UNT N2,ENGI11,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 2
          ON,ENMT3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          PN,ENMT4,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          ON,ENEV3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Novo Mercado
          ON,EGIE3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Novo Mercado
          ON,EQMA3B,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Balcão Organizado
          PNA,EQMA5B,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Balcão Organizado
          PNB,EQMA6B,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Balcão Organizado
          ON,EQPA3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          PNA,EQPA5,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          PNB,EQPA6,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          PNC,EQPA7,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          ON,EQTL3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Novo Mercado
          ON,ESTR3,Outras outras indústrias,Consumo cíclico,Viagens e lazer,Brinquedos e jogos,Tradicional
          PN,ESTR4,Outras outras indústrias,Consumo cíclico,Viagens e lazer,Brinquedos e jogos,Tradicional
          ON,ETER3,Indústria de outros produtos de minerais não metálicos,Bens industriais,Construção e engenharia,Produtos para construção,Novo Mercado
          ON,EUCA3,Indústria de produtos de madeira compensada e afins,Materiais básicos,Madeira e papel,Madeira,Nível 1
          PN,EUCA4,Indústria de produtos de madeira compensada e afins,Materiais básicos,Madeira e papel,Madeira,Nível 1
          ON,EVEN3,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Novo Mercado
          ON,BAUH3,Outras indústrias de alimentos,Consumo não cíclico,Alimentos processados,Carnes e derivados,Tradicional
          PN,BAUH4,Outras indústrias de alimentos,Consumo não cíclico,Alimentos processados,Carnes e derivados,Tradicional
          ON,EZTC3,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Novo Mercado
          ON,FHER3,Indústria de fertilizantes e pesticidas,Materiais básicos,Químicos,Fertilizantes e defensivos,Novo Mercado
          ON,FESA3,Fundição,Materiais básicos,Siderurgia e metalurgia,Siderurgia,Nível 1
          PN,FESA4,Fundição,Materiais básicos,Siderurgia e metalurgia,Siderurgia,Nível 1
          ON,FNCN3,Bancos,Financeiro,Intermediários financeiros,Soc. crédito e financiamento,Tradicional
          ON,FLRY3,Laboratório de exames médicos,Saúde,Serviços médico-hospitalares análises e diagnósticos,Serviços médico-hospitalares análises e diagnósticos,Novo Mercado
          ON,FLEX3,Outros serviços de apoio,Bens industriais,Serviços diversos,Serviços diversos,Bovespa Mais
          ON,FRAS3,Indústria de autopeças,Bens industriais,Material de transporte,Material rodoviário,Nível 1
          ON,GFSA3,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Novo Mercado
          ON,OPGM3B,Administração de empresas e empreendimentos,Financeiro,Outros,Outros,Balcão Organizado
          ON,GSHP3,Locadora de imóveis,Financeiro,Exploração de imóveis,Exploração de imóveis,Novo Mercado
          ON,GEPA3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          PN,GEPA4,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          ON,GGBR3,Transformação de aço em produtos de aço,Materiais básicos,Siderurgia e metalurgia,Siderurgia,Nível 1
          PN,GGBR4,Transformação de aço em produtos de aço,Materiais básicos,Siderurgia e metalurgia,Siderurgia,Nível 1
          ON,GOAU3,Transformação de aço em produtos de aço,Materiais básicos,Siderurgia e metalurgia,Siderurgia,Nível 1
          PN,GOAU4,Transformação de aço em produtos de aço,Materiais básicos,Siderurgia e metalurgia,Siderurgia,Nível 1
          PN,GOLL4,Transporte aéreo regular,Bens industriais,Transporte,Transporte aéreo,Nível 2
          A,GPIV33,Administração de empresas e empreendimentos,Financeiro,Serviços financeiros diversos,Gestão de recursos e investimentos,BDR nível 3
          ON,GPCP3,Administração de empresas e empreendimentos,Materiais básicos,Químicos,Petroquímicos,Tradicional
          PN,GPCP4,Administração de empresas e empreendimentos,Materiais básicos,Químicos,Petroquímicos,Tradicional
          ON,CGRA3,Loja de roupas,Consumo cíclico,Comércio,Tecidos vestuário e calçados,Tradicional
          PN,CGRA4,Loja de roupas,Consumo cíclico,Comércio,Tecidos vestuário e calçados,Tradicional
          ON,GRND3,Indústria de calçados,Consumo cíclico,Tecidos vestuário e calçados,Calçados,Novo Mercado
          ON,NTCO3,Comércio atacadista de bens não duráveis variados,Consumo não cíclico,Produtos de uso pessoal e de limpeza,Produtos de uso pessoal,Novo Mercado
          ON,GUAR3,Indústria de roupas de tecido,Consumo cíclico,Comércio,Tecidos vestuário e calçados,Tradicional
          ON,HBTS3,Administração de empresas e empreendimentos,Financeiro,Exploração de imóveis,Holdings diversificadas,Tradicional
          PNA,HBTS5,Administração de empresas e empreendimentos,Financeiro,Exploração de imóveis,Holdings diversificadas,Tradicional
          PNB,HBTS6,Administração de empresas e empreendimentos,Financeiro,Exploração de imóveis,Holdings diversificadas,Tradicional
          ON,HAGA3,Indústria de ferragens,Bens industriais,Construção e engenharia,Produtos para construção,Tradicional
          PN,HAGA4,Indústria de ferragens,Bens industriais,Construção e engenharia,Produtos para construção,Tradicional
          ON,HAPV3,Serviços ambulatoriais de saúde,Saúde,Serviços médico-hospitalares análises e diagnósticos,Serviços médico-hospitalares análises e diagnósticos,Novo Mercado
          ON,HBOR3,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Novo Mercado
          ON,HETA3,Indústria de ferramentas de metal não motorizadas e cutelaria,Consumo cíclico,Utilidades domésticas,Utensílios domésticos,Tradicional
          PN,HETA4,Indústria de ferramentas de metal não motorizadas e cutelaria,Consumo cíclico,Utilidades domésticas,Utensílios domésticos,Tradicional
          ON,HOOT3,Hotel; motel ou similar,Consumo cíclico,Hotéis e restaurantes,Hotelaria,Tradicional
          PN,HOOT4,Hotel; motel ou similar,Consumo cíclico,Hotéis e restaurantes,Hotelaria,Tradicional
          ON,HYPE3,Outras outras indústrias,Saúde,Comércio e distribuição,Medicamentos e outros produtos,Novo Mercado
          ON,IDNT3,Editoras de software,Tecnologia da informação,Serviços financeiros diversos,Programas e serviços,Tradicional
          ON,IGBR3,Indústria de equipamentos de áudio e vídeo,Consumo cíclico,Exploração de imóveis,Eletrodomésticos,Tradicional
          ON,IGSN3,Água; esgoto e outros sistemas,Utilidade pública,Água e saneamento,Água e saneamento,Bovespa Mais
          ON,IGTA3,Locadora de imóveis,Financeiro,Exploração de imóveis,Exploração de imóveis,Novo Mercado
          ON,PARD3,Laboratório de exames médicos,Saúde,Serviços médico-hospitalares análises e diagnósticos,Serviços médico-hospitalares análises e diagnósticos,Novo Mercado
          ON,MEAL3,Loja de comida e bebida,Consumo cíclico,Hotéis e restaurantes,Restaurante e similares,Novo Mercado
          ON,CATA3,Tecelagens,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          PN,CATA4,Tecelagens,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          ON,ROMI3,Indústria de máquinas industriais,Bens industriais,Máquinas e equipamentos,Máq. e equip. industriais,Novo Mercado
          ON,IDVL3,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 2
          PN,IDVL4,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 2
          ON,INEP3,Outras outras indústrias,Bens industriais,Máquinas e equipamentos,Máq. e equip. industriais,Tradicional
          PN,INEP4,Outras outras indústrias,Bens industriais,Máquinas e equipamentos,Máq. e equip. industriais,Tradicional
          ON,INNT3,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Bovespa Mais
          ON,GNDI3,Laboratório de exames médicos,Saúde,Serviços médico-hospitalares análises e diagnósticos,Serviços médico-hospitalares análises e diagnósticos,Novo Mercado
          ON,IVPR3B,Atividades auxiliares ao transporte rodoviário,Bens industriais,Transporte,Exploração de rodovias,Balcão Organizado
          PN,IVPR4B,Atividades auxiliares ao transporte rodoviário,Bens industriais,Transporte,Exploração de rodovias,Balcão Organizado
          ON,FIGE3,Administração de empresas e empreendimentos,Financeiro,Outros,Outros,Tradicional
          PN,FIGE4,Administração de empresas e empreendimentos,Financeiro,Outros,Outros,Tradicional
          ON,MYPK3,Indústria de autopeças,Consumo cíclico,Automóveis e motocicletas,Automóveis e motocicletas,Novo Mercado
          ON,IRBR3,Seguradora e corretora de seguros,Financeiro,Previdência e seguros,Seguradoras,Novo Mercado
          ON,ITSA3,Administração de empresas e empreendimentos,Financeiro,Intermediários financeiros,Bancos,Nível 1
          PN,ITSA4,Administração de empresas e empreendimentos,Financeiro,Intermediários financeiros,Bancos,Nível 1
          ON,ITUB3,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 1
          PN,ITUB4,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 1
          ON,JBDU3,Indústria de alimentos,Financeiro,Outros,Holdings diversificadas,Tradicional
          PN,JBDU4,Indústria de alimentos,Financeiro,Outros,Holdings diversificadas,Tradicional
          ON,JBSS3,Abatedouros,Consumo não cíclico,Alimentos processados,Carnes e derivados,Novo Mercado
          ON,JPSA3,Administração de empresas e empreendimentos,Financeiro,Exploração de imóveis,Exploração de imóveis,Tradicional
          PN,JPSA4,Administração de empresas e empreendimentos,Financeiro,Exploração de imóveis,Exploração de imóveis,Tradicional
          ON,JHSF3,Construção,Consumo cíclico,Construção civil,Incorporações,Novo Mercado
          ON,JFEN3,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Tradicional
          ON,JOPA3,Moinho de grãos,Consumo não cíclico,Alimentos processados,Alimentos diversos,Tradicional
          PN,JOPA4,Moinho de grãos,Consumo não cíclico,Alimentos processados,Alimentos diversos,Tradicional
          ON,JSLG3,Transporte rodoviário,Bens industriais,Transporte,Transporte rodoviário,Novo Mercado
          ON,CTKA3,Indústria de roupas de tecido,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          PN,CTKA4,Indústria de roupas de tecido,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          ON,KEPL3,Indústria de estruturas metálicas,Bens industriais,Máquinas e equipamentos,Máq. e equip. industriais,Tradicional
          ON,KLBN3,Indústria de papel; celulose e papelão,Materiais básicos,Madeira e papel,Papel e celulose,Nível 2
          PN,KLBN4,Indústria de papel; celulose e papelão,Materiais básicos,Madeira e papel,Papel e celulose,Nível 2
          UNT N2,KLBN11,Indústria de papel; celulose e papelão,Materiais básicos,Madeira e papel,Papel e celulose,Nível 2
          ON,LLIS3,Tecelagens,Consumo cíclico,Comércio,Tecidos vestuário e calçados,Novo Mercado
          ON,LMED3,-,-,-,-,Bovespa Mais
          ON,LIGT3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Novo Mercado
          ON,LINX3,Editoras de software,Tecnologia da informação,Programas e serviços,Programas e serviços,Novo Mercado
          ON,LIQO3,Serviços de apoio a empresas,Bens industriais,Serviços diversos,Serviços diversos,Novo Mercado
          ON,LTEL3B,Mineração de metais,Materiais básicos,Mineração,Minerais metálicos,Balcão Organizado
          PRB,LTEL11B,Mineração de metais,Materiais básicos,Mineração,Minerais metálicos,Balcão Organizado
          ON,LTLA3B,Mineração (exceto petróleo e gás),Materiais básicos,Mineração,Minerais metálicos,Balcão Organizado
          ON,RENT3,Locadora de automóveis,Consumo cíclico,Diversos,Aluguel de carros,Novo Mercado
          ON,LCAM3,Locadora de automóveis,Consumo cíclico,Diversos,Aluguel de carros,Novo Mercado
          ON,LWSA3,Editoras de software,Tecnologia da informação,Programas e serviços,Programas e serviços,Novo Mercado
          ON,LOGG3,Construção,Financeiro,Exploração de imóveis,Exploração de imóveis,Novo Mercado
          ON,LOGN3,Atividades auxiliares ao transporte,Bens industriais,Transporte,Transporte hidroviário,Novo Mercado
          ON,LAME3,Loja de departamentos,Consumo cíclico,Comércio,Produtos diversos,Nível 1
          PN,LAME4,Loja de departamentos,Consumo cíclico,Comércio,Produtos diversos,Nível 1
          ON,AMAR3,Loja de roupas,Consumo cíclico,Comércio,Tecidos vestuário e calçados,Novo Mercado
          ON,LREN3,Loja de roupas,Consumo cíclico,Comércio,Tecidos vestuário e calçados,Novo Mercado
          ON,SPRT3B,Administração de empresas e empreendimentos,Financeiro,Outros,Outros,Balcão Organizado
          ON,LPSB3,Atividades relacionadas a imóveis,Financeiro,Exploração de imóveis,Intermediação imobiliária,Novo Mercado
          ON,LUPA3,Forjarias e estamparias,Petróleo gás e biocombustíveis,Petróleo gás e biocombustíveis,Equipamentos e serviços,Novo Mercado
          ON,MDIA3,Outras indústrias de alimentos,Consumo não cíclico,Alimentos processados,Alimentos diversos,Novo Mercado
          ON,MSRO3,Locadora de automóveis,Consumo cíclico,Diversos,Aluguel de carros,Bovespa Mais
          ON,MGLU3,Loja de departamentos,Consumo cíclico,Comércio,Eletrodomésticos,Novo Mercado
          ON,MGEL3,Forjarias e estamparias,Materiais básicos,Siderurgia e metalurgia,Artefatos de ferro e aço,Tradicional
          PN,MGEL4,Forjarias e estamparias,Materiais básicos,Siderurgia e metalurgia,Artefatos de ferro e aço,Tradicional
          ON,POMO3,Indústria de carrocerias e trailers,Bens industriais,Material de transporte,Material rodoviário,Nível 2
          PN,POMO4,Indústria de carrocerias e trailers,Bens industriais,Material de transporte,Material rodoviário,Nível 2
          ON,MRFG3,Abatedouros,Consumo não cíclico,Alimentos processados,Carnes e derivados,Novo Mercado
          ON,MSPA3,Indústria de produtos de papel e papelão,Consumo cíclico,Madeira e papel,Jornais livros e revistas,Tradicional
          PN,MSPA4,Indústria de produtos de papel e papelão,Consumo cíclico,Madeira e papel,Jornais livros e revistas,Tradicional
          ON,MEND3,Outras construções pesadas e de engenharia civil,Bens industriais,Construção e engenharia,Construção pesada,Tradicional
          PNA,MEND5,Outras construções pesadas e de engenharia civil,Bens industriais,Construção e engenharia,Construção pesada,Tradicional
          PNB,MEND6,Outras construções pesadas e de engenharia civil,Bens industriais,Construção e engenharia,Construção pesada,Tradicional
          ON,MNZC3B,Outras atividades auxiliares ao transporte,Financeiro,Exploração de imóveis,Exploração de imóveis,Balcão Organizado
          ON,BMEB3,Bancos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          PN,BMEB4,Bancos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          ON,MERC3,Bancos,Financeiro,Intermediários financeiros,Soc. crédito e financiamento,Tradicional
          PN,MERC4,Bancos,Financeiro,Intermediários financeiros,Soc. crédito e financiamento,Tradicional
          ON,BMIN3,Bancos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          PN,BMIN4,Bancos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          ON,MTIG3,Outras indústrias de produtos de metal,Materiais básicos,Embalagens,Embalagens,Tradicional
          PN,MTIG4,Outras indústrias de produtos de metal,Materiais básicos,Embalagens,Embalagens,Tradicional
          ON,LEVE3,Indústria de autopeças,Consumo cíclico,Automóveis e motocicletas,Automóveis e motocicletas,Novo Mercado
          ON,FRIO3,Indústria de equipamentos de refrigeração,Bens industriais,Máquinas e equipamentos,Máq. e equip. industriais,Novo Mercado
          ON,MTSA3,Outras indústrias de produtos de metal,Bens industriais,Máquinas e equipamentos,Máq. e equip. construção e agrícolas,Tradicional
          PN,MTSA4,Outras indústrias de produtos de metal,Bens industriais,Máquinas e equipamentos,Máq. e equip. construção e agrícolas,Tradicional
          ON,MILS3,Serviços de engenharia e arquitetura,Bens industriais,Construção e engenharia,Serviços diversos,Novo Mercado
          ON,MMAQ3,Concessionárias de outros veículos motorizados,Bens industriais,Comércio,Material de transporte,Tradicional
          PN,MMAQ4,Concessionárias de outros veículos motorizados,Bens industriais,Comércio,Material de transporte,Tradicional
          ON,BEEF3,Abatedouros,Consumo não cíclico,Alimentos processados,Carnes e derivados,Novo Mercado
          ON,MNPR3,Abatedouros,Consumo não cíclico,Alimentos processados,Carnes e derivados,Tradicional
          ON,MTRE3,Construção de edifícios residenciais,Consumo não cíclico,Construção civil,Incorporações,Novo Mercado
          ON,MMXM3,Mineração de metais,Materiais básicos,Mineração,Minerais metálicos,Novo Mercado
          ON,MOAR3,Administração de empresas e empreendimentos,Financeiro,Holdings diversificadas,Holdings diversificadas,Tradicional
          ON,MOVI3,Locadora de automóveis,Consumo cíclico,Diversos,Aluguel de carros,Novo Mercado
          ON,MRSA3B,Transporte ferroviário,Bens industriais,Transporte,Transporte ferroviário,Balcão Organizado
          PNA,MRSA5B,Transporte ferroviário,Bens industriais,Transporte,Transporte ferroviário,Balcão Organizado
          PNB,MRSA6B,Transporte ferroviário,Bens industriais,Transporte,Transporte ferroviário,Balcão Organizado
          ON,MRVE3,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Novo Mercado
          ON,MULT3,Locadora de imóveis,Financeiro,Exploração de imóveis,Exploração de imóveis,Nível 2
          ON,MNDL3,Indústria de ferragens,Consumo cíclico,Tecidos vestuário e calçados,Acessórios,Tradicional
          ON,NAFG3,Indústria de vidro e produtos de vidro,Consumo cíclico,Utilidades domésticas,Utensílios domésticos,Tradicional
          PN,NAFG4,Indústria de vidro e produtos de vidro,Consumo cíclico,Utilidades domésticas,Utensílios domésticos,Tradicional
          ON,NEOE3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Novo Mercado
          ON,BNBR3,Bancos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          ON,NORD3,Indústria de outros tipos de máquinas,Bens industriais,Máquinas e equipamentos,Máq. e equip. industriais,Tradicional
          ON,NRTQ3,Indústria de remédios,Saúde,Medicamentos e outros produtos,Medicamentos e outros produtos,Bovespa Mais
          ON,NUTR3,Indústria de fertilizantes e pesticidas,Materiais básicos,Químicos,Fertilizantes e defensivos,Bovespa Mais
          ON,ODER3,Indústria de frutas e vegetais em conserva e comidas especiais,Consumo não cíclico,Alimentos processados,Alimentos diversos,Tradicional
          PN,ODER4,Indústria de frutas e vegetais em conserva e comidas especiais,Consumo não cíclico,Alimentos processados,Alimentos diversos,Tradicional
          ON,ODPV3,Consultório odontológico,Saúde,Serviços médico-hospitalares análises e diagnósticos,Serviços médico-hospitalares análises e diagnósticos,Novo Mercado
          ON,OIBR3,Telecomunicações,Comunicações,Telecomunicações,Telecomunicações,Nível 1
          PN,OIBR4,Telecomunicações,Comunicações,Telecomunicações,Telecomunicações,Nível 1
          ON,OMGE3,Administração de empresas e empreendimentos,Utilidade pública,Energia elétrica,Energia elétrica,Novo Mercado
          ON,OPHE3B,Administração de empresas e empreendimentos,Financeiro,Outros,Outros,Balcão Organizado
          ON,OSXB3,Estaleiros,Petróleo gás e biocombustíveis,Petróleo gás e biocombustíveis,Equipamentos e serviços,Novo Mercado
          ON,OFSA3,Indústria de remédios,Saúde,Medicamentos e outros produtos,Medicamentos e outros produtos,Novo Mercado
          ON,PCAR3,Loja de departamentos,Consumo não cíclico,Comércio e distribuição,Alimentos,Nível 1
          PN,PCAR4,Loja de departamentos,Consumo não cíclico,Comércio e distribuição,Alimentos,Nível 1
          ON,PATI3,Transformação de aço em produtos de aço,Materiais básicos,Siderurgia e metalurgia,Artefatos de ferro e aço,Tradicional
          PN,PATI4,Transformação de aço em produtos de aço,Materiais básicos,Siderurgia e metalurgia,Artefatos de ferro e aço,Tradicional
          ON,PEAB3,Administração de empresas e empreendimentos,Financeiro,Holdings diversificadas,Holdings diversificadas,Tradicional
          PN,PEAB4,Administração de empresas e empreendimentos,Financeiro,Holdings diversificadas,Holdings diversificadas,Tradicional
          ON,PMAM3,Outras indústrias de produtos de metal,Materiais básicos,Siderurgia e metalurgia,Artefatos de cobre,Novo Mercado
          ON,PDGR3,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Novo Mercado
          ON,RPMG3,Indústria de produtos de petróleo e carvão,Petróleo gás e biocombustíveis,Petróleo gás e biocombustíveis,Exploração refino e distribuição,Tradicional
          ON,PETR3,Extração de petróleo e gás,Petróleo gás e biocombustíveis,Petróleo gás e biocombustíveis,Exploração refino e distribuição,Nível 2
          PN,PETR4,Extração de petróleo e gás,Petróleo gás e biocombustíveis,Petróleo gás e biocombustíveis,Exploração refino e distribuição,Nível 2
          ON,BRDT3,Comércio atacadista de petróleo e produtos de petróleo,Petróleo gás e biocombustíveis,Petróleo gás e biocombustíveis,Exploração refino e distribuição,Novo Mercado
          ON,PRIO3,Extração de petróleo e gás,Petróleo gás e biocombustíveis,Petróleo gás e biocombustíveis,Exploração refino e distribuição,Novo Mercado
          ON,PTNT3,Tecelagens,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          PN,PTNT4,Tecelagens,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          ON,PINE3,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 2
          PN,PINE4,Bancos,Financeiro,Intermediários financeiros,Bancos,Nível 2
          ON,PLAS3,Indústria de autopeças,Consumo cíclico,Automóveis e motocicletas,Automóveis e motocicletas,Tradicional
          ON,PPAR3,Administração de empresas e empreendimentos,Financeiro,Outros,Outros,Tradicional
          ON,FRTA3,Cultivo de frutas e nozes,Consumo não cíclico,Agropecuária,Agricultura,Novo Mercado
          ON,PSSA3,Seguradora,Financeiro,Previdência e seguros,Seguradoras,Novo Mercado
          ON,PTBL3,Indústria de produtos de cerâmica e refratários,Bens industriais,Construção e engenharia,Produtos para construção,Novo Mercado
          ON,POSI3,Indústria de computadores e periféricos,Tecnologia da informação,Computadores e equipamentos,Computadores e equipamentos,Novo Mercado
          UNT,PPLA11,Instituição de intermediação de crédito e atividades relacionadas,Financeiro,Serviços financeiros diversos,Gestão de recursos e investimentos,Tradicional
          ON,PTCA3,Indústria de eletrodomésticos,Bens industriais,Máquinas e equipamentos,Máq. e equip. industriais,Bovespa Mais Nível 2
          PN Resg,PTCA11,Indústria de eletrodomésticos,Bens industriais,Máquinas e equipamentos,Máq. e equip. industriais,Bovespa Mais Nível 2
          ON,PRNR3,Construção de edifícios residenciais,Bens industriais,Serviços diversos,Serviços diversos,Bovespa Mais
          ON,PFRM3,Comércio atacadista de remédios,Saúde,Comércio e distribuição,Medicamentos e outros produtos,Novo Mercado
          ON,PRPT3B,Administração de empresas e empreendimentos,Financeiro,Outros,Outros,Balcão Organizado
          ON,QUAL3,Outros serviços ambulatoriais de saúde,Saúde,Serviços médico-hospitalares análises e diagnósticos,Serviços médico-hospitalares análises e diagnósticos,Novo Mercado
          ON,QUSW3,Editoras de software,Tecnologia da informação,Programas e serviços,Programas e serviços,Bovespa Mais
          ON,RADL3,Loja de artigos para saúde e cuidados pessoais,Saúde,Comércio e distribuição,Medicamentos e outros produtos,Novo Mercado
          ON,RAPT3,Indústria de carrocerias e trailers,Bens industriais,Material de transporte,Material rodoviário,Nível 1
          PN,RAPT4,Indústria de carrocerias e trailers,Bens industriais,Material de transporte,Material rodoviário,Nível 1
          ON,RCSL3,Indústria de carrocerias e trailers,Bens industriais,Material de transporte,Material rodoviário,Tradicional
          PN,RCSL4,Indústria de carrocerias e trailers,Bens industriais,Material de transporte,Material rodoviário,Tradicional
          ON,REDE3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          PN,REDE4,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          ON,RNEW3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 2
          PN,RNEW4,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 2
          UNT N2,RNEW11,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 2
          ON,RSUL3,Indústria de autopeças,Bens industriais,Material de transporte,Material rodoviário,Tradicional
          PN,RSUL4,Indústria de autopeças,Bens industriais,Material de transporte,Material rodoviário,Tradicional
          ON,RDNI3,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Novo Mercado
          ON,RSID3,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Novo Mercado
          ON,RAIL3,Transporte ferroviário,Bens industriais,Transporte,Transporte ferroviário,Novo Mercado
          ON,SBSP3,Água; esgoto e outros sistemas,Utilidade pública,Água e saneamento,Água e saneamento,Novo Mercado
          ON,SAPR3,Água; esgoto e outros sistemas,Utilidade pública,Água e saneamento,Água e saneamento,Nível 2
          PN,SAPR4,Água; esgoto e outros sistemas,Utilidade pública,Água e saneamento,Água e saneamento,Nível 2
          UNT N2,SAPR11,Água; esgoto e outros sistemas,Utilidade pública,Água e saneamento,Água e saneamento,Nível 2
          ON,SNSY3,Indústria de produtos de plástico,Materiais básicos,Materiais diversos,Materiais diversos,Tradicional
          PNA,SNSY5,Indústria de produtos de plástico,Materiais básicos,Materiais diversos,Materiais diversos,Tradicional
          PNB,SNSY6,Indústria de produtos de plástico,Materiais básicos,Materiais diversos,Materiais diversos,Tradicional
          ON,SANB3,Bancos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          PN,SANB4,Bancos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          UNT,SANB11,Bancos,Financeiro,Intermediários financeiros,Bancos,Tradicional
          ON,CTSA3,Tecelagens,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          PN,CTSA4,Tecelagens,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          PND,CTSA8,Tecelagens,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          ON,STBP3,Atividades auxiliares ao transporte aquático,Bens industriais,Transporte,Serviços de apoio e armazenagem,Novo Mercado
          ON,SCAR3,Locadora de imóveis,Financeiro,Exploração de imóveis,Exploração de imóveis,Novo Mercado
          ON,SMTO3,Indústria de açúcar e produtos de confeitaria,Consumo não cíclico,Alimentos processados,Açúcar e álcool,Novo Mercado
          ON,SLED3,Editoras de jornais; revistas; livros e similares,Consumo cíclico,Comércio,Produtos diversos,Nível 2
          PN,SLED4,Editoras de jornais; revistas; livros e similares,Consumo cíclico,Comércio,Produtos diversos,Nível 2
          ON,SHUL3,Indústria de autopeças,Bens industriais,Máquinas e equipamentos,Motores compressores e outros,Tradicional
          PN,SHUL4,Indústria de autopeças,Bens industriais,Máquinas e equipamentos,Motores compressores e outros,Tradicional
          ON,CSAB3,Seguradora,Financeiro,Previdência e seguros,Seguradoras,Tradicional
          PN,CSAB4,Seguradora,Financeiro,Previdência e seguros,Seguradoras,Tradicional
          ON,SLCT3B,Telecomunicações,Financeiro,Outros,Outros,Balcão Organizado
          ON,SEER3,Escola de ensino superior,Consumo cíclico,Diversos,Serviços educacionais,Novo Mercado
          ON,CSNA3,Transformação de aço em produtos de aço,Materiais básicos,Siderurgia e metalurgia,Siderurgia,Tradicional
          ON,SQIA3,Editoras de software,Tecnologia da informação,Programas e serviços,Programas e serviços,Novo Mercado
          ON,SLCE3,Agricultura,Consumo não cíclico,Agropecuária,Agricultura,Novo Mercado
          ON,SMFT3,Outras indústrias da recreação,Consumo cíclico,Viagens e lazer,Atividades esportivas,Bovespa Mais Nível 2
          PNAB,SMFT13,Outras indústrias da recreação,Consumo cíclico,Viagens e lazer,Atividades esportivas,Bovespa Mais Nível 2
          PNAE,SMFT14,Outras indústrias da recreação,Consumo cíclico,Viagens e lazer,Atividades esportivas,Bovespa Mais Nível 2
          PNAG,SMFT15,Outras indústrias da recreação,Consumo cíclico,Viagens e lazer,Atividades esportivas,Bovespa Mais Nível 2
          PNB,SMFT6,Outras indústrias da recreação,Consumo cíclico,Viagens e lazer,Atividades esportivas,Bovespa Mais Nível 2
          PNE,SMFT11,Outras indústrias da recreação,Consumo cíclico,Viagens e lazer,Atividades esportivas,Bovespa Mais Nível 2
          PNG,SMFT12,Outras indústrias da recreação,Consumo cíclico,Viagens e lazer,Atividades esportivas,Bovespa Mais Nível 2
          ON,SMLS3,Outros serviços de apoio,Consumo cíclico,Diversos,Programas de fidelização,Novo Mercado
          ON,SOND3,Consultoria administrativa; científica e técnica,Bens industriais,Construção e engenharia,Engenharia consultiva,Tradicional
          PNA,SOND5,Consultoria administrativa; científica e técnica,Bens industriais,Construção e engenharia,Engenharia consultiva,Tradicional
          PNB,SOND6,Consultoria administrativa; científica e técnica,Bens industriais,Construção e engenharia,Engenharia consultiva,Tradicional
          ON,SPRI3,Indústria de eletrodomésticos,Financeiro,Holdings diversificadas,Holdings diversificadas,Tradicional
          PNA,SPRI5,Indústria de eletrodomésticos,Financeiro,Holdings diversificadas,Holdings diversificadas,Tradicional
          PNB,SPRI6,Indústria de eletrodomésticos,Financeiro,Holdings diversificadas,Holdings diversificadas,Tradicional
          ON,SGPS3,Indústria de roupas de tecido,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Novo Mercado
          ON,AHEB3,Outros serviços de apoio,Consumo cíclico,Viagens e lazer,Produção de eventos e shows,Tradicional
          PNA,AHEB5,Outros serviços de apoio,Consumo cíclico,Viagens e lazer,Produção de eventos e shows,Tradicional
          PNB,AHEB6,Outros serviços de apoio,Consumo cíclico,Viagens e lazer,Produção de eventos e shows,Tradicional
          ON,STTR3,Industria de máquinas agrícolas; de construção e mineração,Bens industriais,Máquinas e equipamentos,Máq. e equip. construção e agrícolas,Bovespa Mais
          ON,STKF3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Tradicional
          ON,OPSE3B,Administração de empresas e empreendimentos,Financeiro,Outros,Outros,Balcão Organizado
          ON,OPTS3B,Telecomunicações,Financeiro,Outros,Outros,Balcão Organizado
          ON,SULA3,Seguradora,Financeiro,Previdência e seguros,Seguradoras,Nível 2
          PN,SULA4,Seguradora,Financeiro,Previdência e seguros,Seguradoras,Nível 2
          UNT N2,SULA11,Seguradora,Financeiro,Previdência e seguros,Seguradoras,Nível 2
          ON,NEMO3,Administração de empresas e empreendimentos,Materiais básicos,Madeira e papel,Papel e celulose,Tradicional
          PNA,NEMO5,Administração de empresas e empreendimentos,Materiais básicos,Madeira e papel,Papel e celulose,Tradicional
          PNB,NEMO6,Administração de empresas e empreendimentos,Materiais básicos,Madeira e papel,Papel e celulose,Tradicional
          ON,SUZB3,Indústria de papel; celulose e papelão,Materiais básicos,Madeira e papel,Papel e celulose,Novo Mercado
          ON,TAEE3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 2
          PN,TAEE4,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 2
          UNT N2,TAEE11,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 2
          ON,TASA3,Outras indústrias de produtos de metal,Bens industriais,Máquinas e equipamentos,Armas e munições,Nível 2
          PN,TASA4,Outras indústrias de produtos de metal,Bens industriais,Máquinas e equipamentos,Armas e munições,Nível 2
          ON,TECN3,Outras indústrias,Consumo cíclico,Tecidos vestuário e calçados,Acessórios,Novo Mercado
          ON,TCSA3,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Novo Mercado
          ON,TCNO3,Consultoria administrativa; científica e técnica,Bens industriais,Construção e engenharia,Engenharia consultiva,Tradicional
          PN,TCNO4,Consultoria administrativa; científica e técnica,Bens industriais,Construção e engenharia,Engenharia consultiva,Tradicional
          ON,TGMA3,Atividades auxiliares ao transporte,Bens industriais,Transporte,Transporte rodoviário,Novo Mercado
          ON,TEKA3,Indústria de roupas de tecido,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          PN,TEKA4,Indústria de roupas de tecido,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          ON,TKNO3,Outras indústrias de produtos de metal,Materiais básicos,Siderurgia e metalurgia,Artefatos de ferro e aço,Tradicional
          PN,TKNO4,Outras indústrias de produtos de metal,Materiais básicos,Siderurgia e metalurgia,Artefatos de ferro e aço,Tradicional
          ON,TELB3,Telecomunicações,Comunicações,Telecomunicações,Telecomunicações,Tradicional
          PN,TELB4,Telecomunicações,Comunicações,Telecomunicações,Telecomunicações,Tradicional
          ON,VIVT3,Telecomunicações,Comunicações,Telecomunicações,Telecomunicações,Tradicional
          PN,VIVT4,Telecomunicações,Comunicações,Telecomunicações,Telecomunicações,Tradicional
          ON,TEND3,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Novo Mercado
          ON,TESA3,Outras outras indústrias,Consumo não cíclico,Agropecuária,Agricultura,Novo Mercado
          ON,TXRX3,Tecelagens,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          PN,TXRX4,Tecelagens,Consumo cíclico,Tecidos vestuário e calçados,Fios e tecidos,Tradicional
          ON,TIMP3,Telecomunicações,Comunicações,Telecomunicações,Telecomunicações,Novo Mercado
          ON,SHOW3,Apresentações artísticas,Consumo cíclico,Viagens e lazer,Produção de eventos e shows,Novo Mercado
          ON,TOTS3,Editoras de software,Tecnologia da informação,Programas e serviços,Programas e serviços,Novo Mercado
          ON,TRPL3,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 1
          PN,TRPL4,Geração; transmissão e distribuição de energia elétrica,Utilidade pública,Energia elétrica,Energia elétrica,Nível 1
          ON,LUXM3,Administração de empresas e empreendimentos,Bens industriais,Transporte,Transporte hidroviário,Tradicional
          PN,LUXM4,Administração de empresas e empreendimentos,Bens industriais,Transporte,Transporte hidroviário,Tradicional
          ON,TRIS3,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Novo Mercado
          ON,TPIS3,Atividades auxiliares ao transporte rodoviário,Bens industriais,Transporte,Exploração de rodovias,Novo Mercado
          ON,TUPY3,Indústria de autopeças,Bens industriais,Material de transporte,Material rodoviário,Novo Mercado
          ON,UGPA3,Comércio atacadista de petróleo e produtos de petróleo,Petróleo gás e biocombustíveis,Petróleo gás e biocombustíveis,Exploração refino e distribuição,Novo Mercado
          ON,UCAS3,Indústria de móveis e afins,Consumo cíclico,Utilidades domésticas,Móveis,Novo Mercado
          ON,UNIP3,Indústria química,Materiais básicos,Químicos,Químicos diversos,Tradicional
          PNA,UNIP5,Indústria química,Materiais básicos,Químicos,Químicos diversos,Tradicional
          PNB,UNIP6,Indústria química,Materiais básicos,Químicos,Químicos diversos,Tradicional
          ON,UPKP3B,Empresa de eletricidade; gás e água,Utilidade pública,Energia elétrica,Energia elétrica,Balcão Organizado
          ON,USIM3,Transformação de aço em produtos de aço,Materiais básicos,Siderurgia e metalurgia,Siderurgia,Nível 1
          PNA,USIM5,Transformação de aço em produtos de aço,Materiais básicos,Siderurgia e metalurgia,Siderurgia,Nível 1
          PNB,USIM6,Transformação de aço em produtos de aço,Materiais básicos,Siderurgia e metalurgia,Siderurgia,Nível 1
          ON,VALE3,Mineração de metais,Materiais básicos,Mineração,Minerais metálicos,Novo Mercado
          ON,VLID3,Impressão e atividades auxiliares,Bens industriais,Serviços diversos,Serviços diversos,Novo Mercado
          ON,VVAR3,Loja de departamentos,Consumo cíclico,Comércio,Eletrodomésticos,Novo Mercado
          ON,VIVA3,Loja de jóias; malas e artigos de couro,Consumo cíclico,Tecidos vestuário e calçados,Acessórios,Novo Mercado
          ON,VIVR3,Construção de edifícios residenciais,Consumo cíclico,Construção civil,Incorporações,Novo Mercado
          ON,VULC3,Indústria de calçados,Consumo cíclico,Tecidos vestuário e calçados,Calçados,Novo Mercado
          ON,WEGE3,Indústria de motores; turbinas e transmissores de energia,Bens industriais,Máquinas e equipamentos,Motores compressores e outros,Novo Mercado
          ON,MWET3,Indústria de autopeças,Bens industriais,Material de transporte,Material rodoviário,Tradicional
          PN,MWET4,Indústria de autopeças,Bens industriais,Material de transporte,Material rodoviário,Tradicional
          ON,WHRL3,Indústria de eletrodomésticos,Consumo cíclico,Utilidades domésticas,Eletrodomésticos,Tradicional
          PN,WHRL4,Indústria de eletrodomésticos,Consumo cíclico,Utilidades domésticas,Eletrodomésticos,Tradicional
          ON,WSON33,Atividades auxiliares ao transporte aquático,Bens industriais,Transporte,Serviços de apoio e armazenagem,BDR nível 3
          ON,WIZS3,Corretora de seguros,Financeiro,Previdência e seguros,Corretoras de seguros,Novo Mercado
          ON,WLMM3,Concessionárias de outros veículos motorizados,Bens industriais,Comércio,Material de transporte,Tradicional
          PN,WLMM4,Concessionárias de outros veículos motorizados,Bens industriais,Comércio,Material de transporte,Tradicional
          ON,YDUQ3,Escola de ensino superior,Consumo cíclico,Diversos,Serviços educacionais,Novo Mercado"""
    download_failed = "QVQP3B,ALEF3B,BRGE7,APTI3,APTI4,FRRN3B,FRRN5B,FRRN6B,BPAR3,BBML3,BETP3B,BRQB3,CABI3B,CACO3B," \
                      "CPTP3B,CCXC3,CMSA3,CMSA4,CNSY3,CEEB6,CRTE3B,CRTE5B,CTCA3,DTCY4,ETRO3B,EQMA5B,EQMA6B,ESTR3," \
                      "FNCN3,FLEX3,OPGM3B,HBTS3,HBTS6,HETA3,IGSN3,CATA3,CATA4,INNT3,IVPR3B,IVPR4B,JPSA4,LMED3,LIQO3," \
                      "LTEL3B,LTEL11B,LTLA3B,SPRT3B,MSRO3,MEND5,MNZC3B,NAFG3,NAFG4,NRTQ3,ODER3,OPHE3B,PCAR4,PINE3," \
                      "PTCA3,PTCA11,PRPT3B,QUSW3,REDE4,RSUL3,CTSA8,SLCT3B,SMFT3,SMFT13,SMFT14,SMFT15,SMFT6,SMFT11," \
                      "SMFT12,SOND3,STTR3,STKF3,OPSE3B,OPTS3B,NEMO3,NEMO5,NEMO6,UPKP3B".split(",")

    ls = txt.split("\n")
    ll = [l.split(",") for l in ls if l.split(",")[1] not in download_failed]
    m = np.array(ll)
    keys = np.array([[f"{t}.sa"] for t in m[:, 1]])
    m2 = np.hstack([keys, m[:, 0:1], m[:, 2:]])
    h, d = m2[0], m2[1:]
    df = pd.DataFrame(d, columns=h)
    if df.empty:
        print("Returning empty df.")
    return df
