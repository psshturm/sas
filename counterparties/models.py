from django.db import models
import uuid

# Create your models here.


class Counterparties(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inn = models.PositiveIntegerField(verbose_name="ИНН")
    name = models.CharField(max_length=200, verbose_name='Название контрагента')
    web_site = models.CharField(max_length=200, verbose_name='Сайт', blank=True)
    is_website = models.BooleanField(
        default=False, verbose_name='Работоспособность вебсайта')
    RISK_CHOICES = (
        ('STOP', 'стоп'),
        ('DOP_FOCUS', 'Доп. фокус'),
        ('OK', 'Ок'),
    )

    risk = models.CharField(
        max_length=15, choices=RISK_CHOICES, verbose_name='Риск', blank=True, null=True)
    
    с_time = models.DateTimeField(
        verbose_name='Время обновления', blank=True, null=True)

    R_P_CHOICES = (
        ('STOP', 'Вывод активов, ликвидация'),
        ('DOP_FOCUS', 'Дружественная (в форме присоединения компаний группы, укрупнение)'),
        ('OK', 'Отсутствует либо в форме изменения ОПФ (ОАО -АО)'),
    )
    reorganization_procedure = models.CharField(
        max_length=15, choices=R_P_CHOICES, verbose_name='Наличие процедуры реорганизации', blank=True, null=True)

    C_P_CHOICES = (
        ('STOP', 'Смена'),
        ('DOP_FOCUS', 'Планируется'),
        ('OK', 'Нет и не планируется'),
    )
    change_participants = models.CharField(
        max_length=15, choices=C_P_CHOICES, verbose_name='Смена учредителей / участников', blank=True, null=True)

    C_D_CHOICES = (
        ('STOP', 'Возникновение массового директора'),
        ('DOP_FOCUS', 'Планируется'),
        ('OK', 'Нет и не планируется'),
    )
    change_director = models.CharField(
        max_length=15, choices=C_D_CHOICES, verbose_name='Смена директора', blank=True, null=True)

    C_R_A_CHOICES = (
        ('STOP', 'Смена адреса на  массовый, уход в другой регион'),
        ('DOP_FOCUS', 'Планируется'),
        ('OK', 'Нет и не планируется'),
    )
    change_registration_address = models.CharField(
        max_length=15, choices=C_R_A_CHOICES, verbose_name='Смена адреса регистрации', blank=True, null=True)

    C_C_D_CHOICES = (
        ('STOP', 'Р 13001, новая редакция устава (полномочия, вынезение)'),
        ('DOP_FOCUS', 'Р 13001,  не влияющие на полномочия приятия решений руковдителем и составом участников'),
        ('OK', 'нет'),
    )
    change_constituent_documents = models.CharField(
        max_length=15, choices=C_C_D_CHOICES, verbose_name='Изменение в учредительных документах', blank=True, null=True)

    C_S_C_CHOICES = (
        ('STOP', 'Уменьшение'),
        ('DOP_FOCUS', 'Перераспределение долей'),
        ('OK', 'Отсутствует либо увеличение'),
    )
    change_share_capital = models.CharField(
        max_length=15, choices=C_S_C_CHOICES, verbose_name='Изменение уставного капитала', blank=True, null=True)

    B_P_CHOICES = (
        ('STOP', 'Поданы иски, введена процедура банкротства'),
        ('DOP_FOCUS', 'Имеется сообщение кредитора о намерении подать заявление  о несостоятельности'),
        ('OK', 'Отсутствует'),
    )
    bankruptcy_procedure = models.CharField(
        max_length=15, choices=B_P_CHOICES, verbose_name='Наличие процедуры банкротства', blank=True, null=True)

    P_L_CHOICES = (
        ('STOP', 'Множество судебных споров в качестве ответчика либо на крупные суммы, либо с металлотрейдерами (более 30% от активов)'),
        ('DOP_FOCUS', 'Множество судебных споров либо несколько на крупные суммы в качестве истца, ответчика'),
        ('OK', 'Нет, только по ТК'),
    )
    presence_litigation = models.CharField(
        max_length=15, choices=P_L_CHOICES, verbose_name='Наличие судебных споров', blank=True, null=True)

    E_D_CHOICES = (
        ('STOP', 'Большое количество исполнительныз производство либо крупные исполнительные производства (более 30% от активов)'),
        ('DOP_FOCUS', 'Много, более 5% активов'),
        ('OK', 'Нет, только по ТК'),
    )
    executive_documents = models.CharField(
        max_length=15, choices=E_D_CHOICES, verbose_name='Наличие исполнительных документов', blank=True, null=True)

    U_C_CHOICES = (
        ('STOP', 'Иски от ИФНС, арест счетов, приостановление деятельности,  претензии на крупные суммы  ( > 30 % активов). Проверка по причине хищения гос.средств'),
        ('DOP_FOCUS', 'Просрочка налоговых платежей, есть предписания надзорных органов'),
        ('OK', 'Нет'),
    )
    unresolved_claims = models.CharField(
        max_length=15, choices=U_C_CHOICES, verbose_name='Неурегулированных претензий со стороны /к гос.органам', blank=True, null=True)

    C_H_CHOICES = (
        ('STOP', 'Частые случаи просрочек, иски  на курпные суммы, иски от банка'),
        ('DOP_FOCUS', 'Небольшие просрочки'),
        ('OK', 'Хорошая кредитная история'),
    )
    credit_history = models.CharField(
        max_length=15, choices=C_H_CHOICES, verbose_name='Кредитная история  у контрагентов, поставщиков, заказчиков, в банках', blank=True, null=True)

    R_B_CHOICES = (
        ('STOP', 'Существенное сокращение выручки (более 30%), аномальный рост выручки (более 50%)'),
        ('DOP_FOCUS', 'Значительное  сокращение выручки (до 30%)'),
        ('OK', 'Рост, развитие'),
    )
    resizing_business = models.CharField(
        max_length=15, choices=R_B_CHOICES, verbose_name='Изменение уставного  капитала', blank=True, null=True)

    C_B_A_CHOICES = (
        ('STOP', 'Резкое снижение основных фондов (производственных, складских)'),
        ('DOP_FOCUS', 'Выбытие ОС и замена на арендованные площади'),
        ('OK', 'Расширение'),
    )
    change_fixed_assets = models.CharField(
        max_length=15, choices=C_B_A_CHOICES, verbose_name='Изменение масштабов бизнеса', blank=True, null=True)
    
    C_D_L_CHOICES = (
        ('STOP', 'Резкое увеличение долговой нагрузки: кредиты и займы (более 30%)'),
        ('DOP_FOCUS', 'Увеличение долговой нагрузки: кредиты и займы (до  30%)'),
        ('OK', 'Без существенных измнений'),
    )
    change_debt_load = models.CharField(
        max_length=15, choices=C_D_L_CHOICES, verbose_name='Изменение долговой нагрузки: займы и кредиты', blank=True, null=True)
    
    C_C_M_CHOICES = (
        ('STOP', 'Смена  команды'),
        ('DOP_FOCUS', '-----'),
        ('OK', 'Без существенных измнений'),
    )
    changes_company_management = models.CharField(
        max_length=15, choices=C_C_M_CHOICES, verbose_name='Изменения в менедженте компаниии', blank=True, null=True)

    C_P_N_CHOICES = (
        ('STOP', 'Недоступные контактные телефоны'),
        ('DOP_FOCUS', 'Невнятные и неконструктивных комментарии при взаимодействии, необснованные обещания'),
        ('OK', 'Доступны'),
    )
    contact_phone_numbers = models.CharField(
        max_length=15, choices=C_P_N_CHOICES, verbose_name='Контактные телефоны', blank=True, null=True)

    I_C_CHOICES = (
        ('STOP', 'Приоставновка финансирования проекта/заказа, существенное смещение сроков оплаты за выполненные работы, иски.'),
        ('DOP_FOCUS', 'Изменение схемы финансирования проектов, сроков выполнения. Расторжение ранее заключенных контрактов. '),
        ('OK', 'Нет негативной информации по работе с Заказчиками'),
    )
    interaction_Customers = models.CharField(
        max_length=15, choices=I_C_CHOICES, verbose_name='Взаимодействие с Заказчиками', blank=True, null=True)

    T_B_CHOICES = (
        ('STOP', 'Выведение внеоборотных активов (перевод на другое юр.лицо)'),
        ('DOP_FOCUS', 'Перераспределение заказов на другое юр.лицо, смещение закупки на другое юр.лицо '),
        ('OK', 'Нет изменений'),
    )
    transfer_of_business = models.CharField(
        max_length=15, choices=T_B_CHOICES, verbose_name='Перевод бизнеса на другое юр.лицо', blank=True, null=True)

    C_S_A_CHOICES = (
        ('STOP', 'Планируется резкая смена деятельности '),
        ('DOP_FOCUS', 'Информация о развитии иных непрофильных проектов, направлений'),
        ('OK', 'Нет изменений'),
    )
    changing_scope_activities = models.CharField(
        max_length=15, choices=C_S_A_CHOICES, verbose_name='Изменение сферы деятельности', blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'
    
    
    def __str__(self):
        return '{} {} {} '.format(self.name, self.inn, self.web_site, self.risk, self.с_time)

class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    counterparty = models.ForeignKey(
        Counterparties, on_delete=models.CASCADE, blank=True, null=True)
    news = models.TextField(verbose_name="Новости")

    
    C_I_CHOICES = (
        ('STOP', 'Кризис в отрасли. Несоответствие компании "новым стандартам". '),
        ('DOP_FOCUS', 'Изменения законодательства.  Введение мер регулирования государством.'),
        ('OK', 'Стабильна, рост'),
    )

    customer_industry = models.CharField(
        max_length=15, choices=C_I_CHOICES, verbose_name='По отрасли клиента', blank=True, null=True)

    M_C_CHOICES = (
        ('STOP', 'Негативные отклики, проблемы у команды, менеджмента компании,  учредителей, негативные отклики на форумах работодателя («черный список работодателей»).  Смена собственника, директора, негативные отзывы о работодателе . Смерть учредителя.   '),
        ('DOP_FOCUS', 'Губернаторский риск: компания под управлением приближенных к губернатору. Ключевые изменения в стратегии управления  компанией, проектами. '),
        ('OK', 'Хорошая репутация. Стабильные связи по проектам или   имеются связи с "приближенными к власти"'),
    )

    management_company = models.CharField(
        max_length=15, choices=M_C_CHOICES, verbose_name='По менеджменту компании', blank=True, null=True)

    C_B_CHOICES = (
        ('STOP', 'Проблемы с проектами. Проблемы с крупным монопроектом.  Иск/иски   от банков.  Реестр недобросоветных поставщиков. Объявления о продаже производственных площадей на авито, др.специализированных сайтах'),
        ('DOP_FOCUS', 'Противоречивый новостной фон (проблемы у группы , у  одной из компаний группы, аффлированного банка)'),
        ('OK', 'Хороший новостной фон по проектам. Новые инвестиционные проекты. Улучшения. Досрочные исполнения.'),
    )

    company_business = models.CharField(
        max_length=15, choices=C_B_CHOICES, verbose_name='По компании как бизнесу', blank=True, null=True)

    O_P_CHOICES = (
        ('STOP', 'Отрицательный новостной  фон, проблемы с проектами/объектами (проблемы с разрешениями на строительство, заморозка проекта, прекращение финансирования проекта), аварии'),
        ('DOP_FOCUS', 'Противоречивый новостной фон по объектам, проектам (проблемы с документацией,  изменение стоимости проекта, изменение схемы  финансирования проекта). Монопроект/монообъект'),
        ('OK', 'Рост портфеля заказов,  проектов. Крупные проекты, анансированные в СМИ'),
    )

    objects_projects = models.CharField(
        max_length=15, choices=O_P_CHOICES, verbose_name='По  объектам, проектам', blank=True, null=True)

    class Meta:
        ordering = ['news']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return '{}'.format(self.objects_projects)


class SparkSettings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cron_key = models.CharField(max_length=200, verbose_name='Периодичность обновления')

    class Meta:
        ordering = ['cron_key']
        verbose_name = 'Настройка СПАРК'
        verbose_name_plural = 'Настройки СПАРК'

    def __str__(self):
        return '{}'.format(self.cron_key)


class NotificationSettings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=200, verbose_name='email для уведомленияы')

    class Meta:
        ordering = ['email']
        verbose_name = 'Настройка уведомлений'
        verbose_name_plural = 'Настройки уведомлений'

    def __str__(self):
        return '{}'.format(self.email)


class SourceSettings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.CharField(max_length=200, verbose_name='url источника')

    class Meta:
        ordering = ['url']
        verbose_name = 'Настройка источников'
        verbose_name_plural = 'Настройки источников'

    def __str__(self):
        return '{}'.format(self.url)
