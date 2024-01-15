# Descarga directa de Boletines oficiales

## Uso

### Manual

`python3 dd.py`

### Cronjob

`0 */4 * * * /usr/local/bin/python3.12 ~/boletin/dd.py; date >> ~/b.log`

Corre cada cuatro horas; ademas nos deja un log de cada ejecucion.


## Docker

## Boletines

Por ahora solo esta incluido el boletin oficial de la nacion; ire incluyendo el de cada provincia.
