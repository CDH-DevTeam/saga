from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
import diana.abstract.models as abstract
from diana.abstract.mixins import GenderedMixin
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Archive(abstract.AbstractBaseModel):
    LEVEL_CHOICE = (
        ('A', 'Avdelning'),
        ('S', 'Serie'),
        ('V', 'Volym'),
        ('O', 'Omslag'),
        ('U1', 'Underserie 1'),
        ('U2', 'Underserie 2')
    )

    name = models.CharField(max_length=255, verbose_name= _("name"), null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name= _("title"), null=True, blank=True)
    level = models.CharField(max_length=4, choices=LEVEL_CHOICE, verbose_name= _("level"), null=True, blank=True)
    parent_name = models.ForeignKey('Archive', on_delete=models.PROTECT, verbose_name= _("parent name"), null=True, blank=True)
    notes = models.TextField(verbose_name= _("notes"), null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("archive")
        verbose_name_plural = _("archives")


class ArtForm(abstract.AbstractBaseModel):
    formname = models.CharField(max_length=255, verbose_name= _("form name"), null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name= _("title"), null=True, blank=True)
    
    def __str__(self):
        return f"{self.formname}"

    class Meta:
        verbose_name = _("art form")
        verbose_name_plural = _("art forms")


class Role(abstract.AbstractBaseModel):
    role_name = models.CharField(verbose_name= _("role"), max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.role_name}"

    class Meta:
        verbose_name = _("role")
        verbose_name_plural = _("roles")

    
class Publisher(abstract.AbstractBaseModel):

    title = models.CharField(max_length=255, verbose_name= _("title"), blank=True, null=True)
    place = models.CharField(max_length=255, verbose_name= _("place"), blank=True, null=True)
    startyear = models.IntegerField(verbose_name= _("start year"), blank=True, null=True)
    endyear = models.IntegerField(verbose_name= _("end year"), blank=True, null=True)
    notes = models.TextField(verbose_name= _("notes"), blank=True, null=True)
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _("publisher")
        verbose_name_plural = _("publishers")


class Series(abstract.AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name= _("name"), blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name= _("title"), blank=True, null=True)
    publisher_title = models.ForeignKey(Publisher, verbose_name= _("publisher title"), on_delete=models.PROTECT, blank=True, null=True)
    startyear = models.IntegerField(verbose_name= _("startyear"), blank=True, null=True)
    endyear = models.IntegerField(verbose_name= _("endyear"), blank=True, null=True)
    notes = models.TextField(verbose_name= _("notes"), blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("series")
        verbose_name_plural = _("series")


class Volume(abstract.AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name= _("name"), blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name= _("title"), blank=True, null=True)
    subtitle = models.CharField(max_length=255, verbose_name= _("subtitle"), blank=True, null=True)
    year = models.IntegerField(verbose_name= _("year"), blank=True, null=True)
    isbn = models.CharField(max_length=255, verbose_name= _("isbn"), blank=True, null=True)
    libris = models.CharField(max_length=255, verbose_name= _("libris"), blank=True, null=True)
    litteraturbanken = models.CharField(max_length=255, verbose_name= _("litteraturbanken"), blank=True, null=True)
    series_name = models.ForeignKey(Series, on_delete=models.PROTECT, verbose_name= _("series name"), blank=True, null=True)
    notes = models.TextField(verbose_name= _("notes"), blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("volume")
        verbose_name_plural = _("volumes")


class Edition(abstract.AbstractBaseModel):

    title = models.CharField(max_length=255, verbose_name= _("title"), blank=True, null=True)
    preface = models.TextField(blank=True, verbose_name= _("pre-face"), null=True)
    backtext = models.TextField(verbose_name= _("back text"), blank=True, null=True)
    paratext = models.TextField(verbose_name= _("para text"), blank=True, null=True)
    num = models.IntegerField(verbose_name= _("num"), blank=True, null=True)
    pages = models.IntegerField(verbose_name= _("pages"), blank=True, null=True)
    year = models.IntegerField(verbose_name= _("year"), blank=True, null=True)
    libris = models.CharField(max_length=255, verbose_name= _("libris"), blank=True, null=True)
    volume_name = models.ForeignKey('Volume', on_delete=models.PROTECT, verbose_name= _("volume name"), blank=True, null=True)
    notes = models.TextField(verbose_name= _("notes"), blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _("edition")
        verbose_name_plural = _("editions")


class SagaText(abstract.AbstractBaseModel):
    VARIANT_CHOICE = (
        ('T', 'Tryckt'),
        ('M', 'Manus 1'),
        ('M2', 'Manus 2'),
        ('M3', 'Manus 3'),

    )
    title = models.CharField(max_length=255, verbose_name= _("title"), blank=True, null=True)
    originaltitle = models.CharField(max_length=255, verbose_name= _("original title"), blank=True, null=True)
    langiso = models.CharField(max_length=4, verbose_name= _("langiso"), blank=True, null=True)
    variant = models.CharField(max_length=255, choices=VARIANT_CHOICE, verbose_name= _("variant"), blank=True, null=True)
    filename = models.CharField(max_length=255, verbose_name= _("file name"), blank=True, null=True)
    pages = models.IntegerField(verbose_name= _("pages"), blank=True, null=True)
    year = models.IntegerField(verbose_name= _("year"), blank=True, null=True)
    archive_name = models.ForeignKey(Archive, verbose_name= _("archive name"), on_delete=models.PROTECT, blank=True, null=True)
    notes = models.TextField(verbose_name= _("notes"), blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _("saga text")
        verbose_name_plural = _("saga texts")


class Illustration(abstract.AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name= _("title"), blank=True, null=True)
    method = models.ForeignKey(ArtForm, on_delete=models.PROTECT, verbose_name= _("method"), blank=True, null=True)
    colour = models.BooleanField(verbose_name= _("colour"),blank=True, null=True)
    filename = models.CharField(max_length=255,verbose_name= _("file name"), blank=True, null=True)
    year = models.IntegerField(verbose_name= _("year"), blank=True, null=True)
    archive_name = models.ForeignKey(Archive, on_delete=models.PROTECT, verbose_name= _("archive name"), blank=True, null=True)
    notes = models.TextField(verbose_name= _("notes"), blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _("illustration")
        verbose_name_plural = _("illustrations")


class Person(abstract.AbstractBaseModel, GenderedMixin):

    lastname = models.CharField(max_length=255, verbose_name= _("lastname"), blank=True, null=True)
    maidenname = models.CharField(max_length=255, verbose_name= _("maidenname"), blank=True, null=True)
    firstname = models.CharField(max_length=255, verbose_name= _("firstname"), blank=True, null=True)
    birthday = models.CharField(max_length=255, verbose_name= _("birthday"), blank=True, null=True)
    deathday = models.CharField(max_length=255, verbose_name= _("deathday"), blank=True, null=True)
    birthplace = models.CharField(max_length=255, verbose_name= _("birthplace"), blank=True, null=True)
    deathplace = models.CharField(max_length=255, verbose_name= _("deathplace"), blank=True, null=True)
    wikidata = models.CharField(max_length=255, verbose_name= _("wikidata"), blank=True, null=True)
    librisxl = models.CharField(max_length=255, verbose_name= _("librisxl"), blank=True, null=True)
    notes = models.TextField(verbose_name= _("notes"), blank=True, null=True)

    def __str__(self):
        return f"{self.lastname}"

    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("persons")


class Place(abstract.AbstractBaseModel):
    placename = models.CharField(max_length=255, verbose_name= _("place name"), blank=True, null=True)
    geom = models.MultiPolygonField(verbose_name= _("geom"), blank=True, null=True)
    wikidata = models.CharField(verbose_name= _("wikidata"), max_length=255, blank=True, null=True)
    parish_id = models.IntegerField(verbose_name= _("parish ID"), blank=True, null=True)
    municipality_id = models.IntegerField(verbose_name= _("municipality ID"), blank=True, null=True)
    notes = models.TextField(verbose_name= _("notes"), blank=True, null=True)


    def __str__(self):
        return f"{self.placename}"

    class Meta:
        verbose_name = _("place")
        verbose_name_plural = _("places")


# Do we need AbstractBaseModel or simple model?     
class RelIllustrEdition(models.Model):
    illustration_title = models.ForeignKey(Illustration, verbose_name= _("illustration title"), on_delete=models.PROTECT, blank=True, null=True)
    edition_title = models.ForeignKey(Edition, verbose_name= _("edition title"), on_delete=models.PROTECT, blank=True, null=True)


class RelPersonIllustration(models.Model):
    person_lastname = models.ForeignKey(Person, verbose_name= _("person lastname"), on_delete=models.PROTECT, blank=True, null=True)
    illustration_title = models.ForeignKey(Illustration, verbose_name= _("illustration title"), on_delete=models.PROTECT, blank=True, null=True)
    role = models.ForeignKey(Role, verbose_name= _("role"), on_delete=models.PROTECT, blank=True, null=True)


class RelPersonText(models.Model):
    person_lastname = models.ForeignKey(Person,verbose_name= _("person lastname"), on_delete=models.PROTECT, blank=True, null=True)
    sagatext_title = models.ForeignKey(SagaText,verbose_name= _("sagatext title"), on_delete=models.PROTECT, blank=True, null=True)
    role = models.ForeignKey(Role, verbose_name= _("role"), on_delete=models.PROTECT, blank=True, null=True)


class RelTextEdition(models.Model):
    sagatext_title = models.ForeignKey(SagaText,verbose_name= _("sagatext title"), on_delete=models.PROTECT, blank=True, null=True)
    edition_title = models.ForeignKey(Edition,verbose_name= _("edition title"), on_delete=models.PROTECT, blank=True, null=True)
