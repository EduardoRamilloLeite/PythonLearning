# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
#cada sistema operacional funciona de uma forma

import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

print(calendar.calendar(2022))