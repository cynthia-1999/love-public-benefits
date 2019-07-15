# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ActVolum(models.Model):
    act_numb = models.AutoField(db_column='Act_numb', primary_key=True)  # Field name made lowercase.
    v_name = models.CharField(db_column='V_name', max_length=50)  # Field name made lowercase.
    v_btime = models.DateField(db_column='V_btime', blank=True, null=True)  # Field name made lowercase.
    v_etime = models.DateField(db_column='V_etime', blank=True, null=True)  # Field name made lowercase.
    v_type = models.ForeignKey('ActInteg', models.DO_NOTHING, db_column='V_type', blank=True, null=True)  # Field name made lowercase.
    v_describe = models.TextField(db_column='V_describe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Act_Volum'


class ActInteg(models.Model):
    v_type = models.CharField(db_column='V_type', primary_key=True, max_length=50)  # Field name made lowercase.
    t_integration = models.IntegerField(db_column='T_integration', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Act_integ'


class ActJoin(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    user_id = models.CharField(db_column='User_ID', max_length=20)  # Field name made lowercase.
    v_numb = models.IntegerField(db_column='V_numb')  # Field name made lowercase.
    j_btime = models.DateField(db_column='J_btime', blank=True, null=True)  # Field name made lowercase.
    j_etime = models.DateField(db_column='J_etime', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Act_join'


class ComJoin(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    cname = models.CharField(max_length=50)
    rea_name = models.CharField(db_column='Rea_name', max_length=50)  # Field name made lowercase.
    res_telenumb = models.CharField(db_column='Res_telenumb', max_length=20)  # Field name made lowercase.
    c_btime = models.DateField(db_column='C_btime', blank=True, null=True)  # Field name made lowercase.
    c_etime = models.DateField(db_column='C_etime', blank=True, null=True)  # Field name made lowercase.
    v_numb = models.IntegerField(blank=True, null=True)
    counts = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Com_join'


class Userinfo(models.Model):
    user_id = models.CharField(db_column='User_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    user_name = models.CharField(db_column='User_name', max_length=50)  # Field name made lowercase.
    user_passwd = models.CharField(db_column='User_passwd', max_length=50)  # Field name made lowercase.
    user_telenumb = models.CharField(db_column='User_telenumb', max_length=50)  # Field name made lowercase.
    user_tname = models.CharField(db_column='User_tname', max_length=50)  # Field name made lowercase.
    user_integration = models.IntegerField(db_column='User_integration', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'UserInfo'

