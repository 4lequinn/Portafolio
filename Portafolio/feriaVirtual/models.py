# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    id_adm = models.CharField(primary_key=True, max_length=15)
    rut_adm = models.IntegerField()
    dv_adm = models.CharField(max_length=1)
    nombre_adm = models.CharField(max_length=30)
    apellido_paterno_adm = models.CharField(max_length=15)
    apellido_materno_adm = models.CharField(max_length=15)
    telefono_adm = models.IntegerField()
    email_adm = models.CharField(max_length=100)
    cuenta_id_cuenta = models.ForeignKey('Cuenta', models.DO_NOTHING, db_column='cuenta_id_cuenta')

    class Meta:
        managed = False
        db_table = 'administrador'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

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
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
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


class Bodega(models.Model):
    id_bodega = models.CharField(primary_key=True, max_length=15)
    stock = models.DecimalField(max_digits=6, decimal_places=2)
    direccion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'bodega'


class Ciudad(models.Model):
    id_ciudad = models.CharField(primary_key=True, max_length=15)
    descripcion_cd = models.CharField(max_length=30)
    pais_id_pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='pais_id_pais')
    cliente_id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente_id_cliente')

    class Meta:
        managed = False
        db_table = 'ciudad'


class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=15)
    nombre_cli = models.CharField(max_length=15)
    apellido_paterno_cli = models.CharField(max_length=15)
    apellido_materno_cli = models.CharField(max_length=15)
    razon_social_cli = models.CharField(max_length=50)
    email_cli = models.CharField(max_length=50)
    telefono_cli = models.BigIntegerField()
    direccion_cli = models.CharField(max_length=50)
    tipo_cliente_id_cliente_tc = models.ForeignKey('TipoCliente', models.DO_NOTHING, db_column='tipo_cliente_id_cliente_tc')
    ciudad_id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_id_ciudad')
    cuenta_id_cuenta = models.ForeignKey('Cuenta', models.DO_NOTHING, db_column='cuenta_id_cuenta')

    class Meta:
        managed = False
        db_table = 'cliente'


class Consultor(models.Model):
    cuenta_id_cuenta = models.ForeignKey('Cuenta', models.DO_NOTHING, db_column='cuenta_id_cuenta')
    id_consultor = models.CharField(primary_key=True, max_length=15)
    rut_ctr = models.IntegerField()
    dv_ctr = models.CharField(max_length=1)
    nombre_ctr = models.CharField(max_length=30)
    apellido_paterno_ctr = models.CharField(max_length=15)
    apellido_materno_ctr = models.CharField(max_length=15)
    telefono_ctr = models.IntegerField()
    email_ctr = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'consultor'


class Contrato(models.Model):
    id_contrato = models.CharField(primary_key=True, max_length=15)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    empresa_id_empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='empresa_id_empresa')
    productor_id_productor = models.ForeignKey('Productor', models.DO_NOTHING, db_column='productor_id_productor')
    vigencia = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'contrato'


class Cuenta(models.Model):
    id_cuenta = models.CharField(primary_key=True, max_length=15)
    usuario = models.CharField(max_length=20)
    contrasenia = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    pregunta_seguridad = models.CharField(max_length=30)
    consultor_id_consultor = models.ForeignKey(Consultor, models.DO_NOTHING, db_column='consultor_id_consultor')
    administrador_id_adm = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='administrador_id_adm')

    class Meta:
        managed = False
        db_table = 'cuenta'


class DetalleVenta(models.Model):
    cantidad_venta = models.IntegerField()
    total_detalle_venta = models.IntegerField()
    descripcion_venta = models.CharField(max_length=30, blank=True, null=True)
    producto_id_producto = models.CharField(primary_key=True, max_length=15)
    subasta_id_venta = models.ForeignKey('Subasta', models.DO_NOTHING, db_column='subasta_id_venta')
    producto_cuenta_id_cuenta = models.CharField(max_length=15)
    id_cliente = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'detalle_venta'
        unique_together = (('producto_id_producto', 'producto_cuenta_id_cuenta', 'subasta_id_venta'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    id_empresa = models.CharField(primary_key=True, max_length=15)
    razon_social_emp = models.CharField(max_length=20)
    nombre_emp = models.CharField(max_length=30)
    rut_emp = models.CharField(max_length=1)
    dv_emp = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'empresa'


class EstadoPedido(models.Model):
    id_estado_pedido = models.CharField(primary_key=True, max_length=15)
    descripcion_ep = models.CharField(max_length=500)
    fecha_creacion = models.DateField()
    subasta_id_venta = models.ForeignKey('Subasta', models.DO_NOTHING, db_column='subasta_id_venta')
    transporte_num_pedido = models.IntegerField()
    fecha_actualizacion = models.DateField()

    class Meta:
        managed = False
        db_table = 'estado_pedido'


class FormaPago(models.Model):
    id_forma_pago = models.CharField(primary_key=True, max_length=50)
    descripcion_fp = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'forma_pago'


class Pais(models.Model):
    id_pais = models.CharField(primary_key=True, max_length=15)
    descripcion_pais = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pais'


class Productor(models.Model):
    id_productor = models.CharField(primary_key=True, max_length=15)
    cuenta_id_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='cuenta_id_cuenta')
    razon_social_pdr = models.CharField(max_length=20)
    rut_pdr = models.IntegerField()
    dv_pdr = models.CharField(max_length=9)
    nombre_pdr = models.CharField(max_length=30)
    apellido_paterno_pdr = models.CharField(max_length=15)
    apellido_materno_pdr = models.CharField(max_length=15)
    telefono_pdr = models.IntegerField()
    email_prd = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'productor'


class Subasta(models.Model):
    id_venta = models.CharField(primary_key=True, max_length=15)
    cliente_id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_cliente')
    total_venta = models.IntegerField()
    productor_id_productor = models.ForeignKey(Productor, models.DO_NOTHING, db_column='productor_id_productor')
    fecha_de_venta = models.DateField(db_column='fecha_de__venta')  # Field renamed because it contained more than one '_' in a row.
    estado_pedido_id_estado_pedido = models.ForeignKey(EstadoPedido, models.DO_NOTHING, db_column='estado_pedido_id_estado_pedido')
    forma_pago_id_forma_pago = models.ForeignKey(FormaPago, models.DO_NOTHING, db_column='forma_pago_id_forma_pago')
    transporte_num_pedido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subasta'


class TipoCliente(models.Model):
    id_cliente_tc = models.CharField(primary_key=True, max_length=15)
    descripcion_tc = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_cliente'


class Transportista(models.Model):
    id_transportista = models.CharField(primary_key=True, max_length=15)
    rut_trs = models.IntegerField()
    dv_trs = models.CharField(max_length=1)
    nombre_trs = models.CharField(max_length=30)
    apellido_paterno_trs = models.CharField(max_length=15)
    apellido_materno_trs = models.CharField(max_length=15)
    telefono_trs = models.IntegerField()
    email_trs = models.CharField(max_length=100)
    cuenta_id_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='cuenta_id_cuenta')

    class Meta:
        managed = False
        db_table = 'transportista'
