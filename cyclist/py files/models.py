# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cyclist(models.Model):
    # Field name made lowercase.
    cyclist_id = models.IntegerField(db_column='Cyclist_id', primary_key=True)
    # Field name made lowercase.
    cyclist_name = models.CharField(
        db_column='Cyclist_name', max_length=50, blank=True, null=True)
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    # Field name made lowercase.
    country = models.CharField(
        db_column='Country', max_length=50, blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    gender = models.TextField(db_column='Gender', blank=True, null=True)
    # Field name made lowercase.
    email_id = models.CharField(
        db_column='Email_id', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cyclist'


class Organizer(models.Model):
    # Field name made lowercase.
    organizer_id = models.IntegerField(
        db_column='Organizer_id', primary_key=True)
    # Field name made lowercase.
    organizer_name = models.CharField(
        db_column='Organizer_name', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    contact = models.CharField(
        db_column='Contact', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    address = models.CharField(
        db_column='Address', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Organizer'

    def __str__(self):
        return str(self.organizer_id)


class Event(models.Model):
    # Field name made lowercase.
    event_id = models.IntegerField(db_column='Event_id', primary_key=True)
    # Field name made lowercase.
    event_name = models.CharField(
        db_column='Event_name', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    event_type = models.CharField(
        db_column='Event_type', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50)
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.TimeField(db_column='Time')  # Field name made lowercase.
    # Field name made lowercase.
    organizer = models.ForeignKey(
        'Organizer', models.DO_NOTHING, db_column='Organizer_id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Event'


class Participant(models.Model):
    # Field name made lowercase.
    event = models.OneToOneField(
        Event, models.DO_NOTHING, db_column='Event_id', primary_key=True)
    # Field name made lowercase.
    cyclist = models.ForeignKey(
        Cyclist, models.DO_NOTHING, db_column='Cyclist_id')
    # Field name made lowercase.
    event_name = models.CharField(db_column='Event_name', max_length=50)
    # Field name made lowercase.
    cyclist_type = models.CharField(
        db_column='Cyclist_type', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cycle_type = models.CharField(
        db_column='Cycle_type', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Participant'
        unique_together = (('event', 'cyclist', 'event_name'),)


class CountryPerformance(models.Model):
    # Field name made lowercase.
    event = models.OneToOneField(
        'Event', models.DO_NOTHING, db_column='Event_id', primary_key=True)
    rank = models.IntegerField(db_column='Rank')  # Field name made lowercase.
    # Field name made lowercase.
    cyclist_country = models.CharField(
        db_column='Cyclist_country', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Country_performance'
        unique_together = (('event', 'rank'),)


class CyclistPerformance(models.Model):
    # Field name made lowercase.
    event = models.OneToOneField(
        'Event', models.DO_NOTHING, db_column='Event_id', primary_key=True)
    # Field name made lowercase.
    event_name = models.CharField(db_column='Event_name', max_length=50)
    rank = models.IntegerField(db_column='Rank')  # Field name made lowercase.
    # Field name made lowercase.
    cyclist = models.ForeignKey(
        Cyclist, models.DO_NOTHING, db_column='Cyclist_id')

    class Meta:
        managed = False
        db_table = 'Cyclist_performance'
        unique_together = (('event', 'event_name', 'rank'),)


class EventSponsor(models.Model):
    # Field name made lowercase.
    event = models.OneToOneField(
        Event, models.DO_NOTHING, db_column='Event_id', primary_key=True)
    # Field name made lowercase.
    sponsor_name = models.ForeignKey(
        'Sponsor', models.DO_NOTHING, db_column='Sponsor_name')
    # Field name made lowercase.
    sponsorship_amount = models.IntegerField(
        db_column='Sponsorship_amount', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Event_sponsor'
        unique_together = (('event', 'sponsor_name'),)


class EventStatus(models.Model):
    # Field name made lowercase.
    event = models.OneToOneField(
        Event, models.DO_NOTHING, db_column='Event_id', primary_key=True)
    # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)
    date = models.DateField(db_column='Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Event_status'
        unique_together = (('event', 'status'),)


class Sponsor(models.Model):
    # Field name made lowercase.
    sponsor_name = models.CharField(
        db_column='Sponsor_name', primary_key=True, max_length=50)
    # Field name made lowercase.
    sponsor_type = models.CharField(
        db_column='Sponsor_type', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    location = models.CharField(
        db_column='Location', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    contact = models.CharField(
        db_column='Contact', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sponsor'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class meta:
    db_table = "Cyclist"
