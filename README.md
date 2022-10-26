# Urna Eletronica

## Pacotes necesários

* python-gnupg
* jsonpickle


##### Execução da aplicação

```shell
python app/__init__.py
```

Para importação das chaves:

```shell
python app/importKeys.py
```

Para a apuração dos votos os arquivos "votos_candidatos.txt" deverão estar na pasta './data/counting-votes'

```shell
python app/countingVotes.py
```

#### Variáveis de ambiente

* `password` - Senha das chaves.
* `gnupghome` - Caminho onde está localizado o gnupg.
* `secao` - Seção eleitoral.