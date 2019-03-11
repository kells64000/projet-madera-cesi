# -*- coding: utf-8 -*-

# Component family

EXTERIOR = 'EX'
INSULATOR = 'IN'
COVER = 'CV'

FAMILY_CHOICES = (
    (EXTERIOR, 'exterior'),
    (INSULATOR, 'insulator'),
    (COVER, 'cover'),
)

# Component material kinds

WOOD = 'WOO'
ROUGH = 'ROU'

MATERIAL_CHOICES = (
    (WOOD, 'wood'),
    (ROUGH, 'roughcast'),
)

# Component nature

SYNTH = 'SYN'
NATURAL = 'NAT'
BIO = 'BIO'

NATURE_CHOICES = (
    (SYNTH, 'synthetic'),
    (NATURAL, 'natural'),
    (BIO, 'biological'),
)

# Gamme type

EXCELLENCE = 'EXL'
LUXE = 'LUX'
NATURAL = 'NAT'

GAMME_CHOICES = (
    (EXCELLENCE, 'excellence'),
    (LUXE, 'luxe'),
    (NATURAL, 'natural'),
)

# House shape

SQUARE = 'SQR'
RECTANGLE = 'REC'
CUSTOM = 'CUS'

SHAPE_CHOICES = (
    (SQUARE, 'square'),
    (RECTANGLE, 'rectangle'),
    (CUSTOM, 'custom'),
)
