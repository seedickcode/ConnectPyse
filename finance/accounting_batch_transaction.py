from ..cw_model import CWModel


class AccountingBatchTransaction(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.batch = None  # (BatchReference)
        self.billingLogId = None  # (Integer)
        self.invoiceNumber = None  # (String)
        self.type = None  # (Enum)
        self.description = None  # (String)
        self.cost = None  # (Number)
        self.item = None  # (String)
        self.inventory = None  # (String)
        self.salesCode = None  # (String)
        self.cogs = None  # (String)
        self.glAccount = None  # (String)
        self.currency = None  # (CurrencyReference)
        self.debitAmount = None  # (Number)
        self.creditAmount = None  # (Number)
        self.balance = None  # (String)
        self.product = None  # (ProductReference)
        self.quantity = None  # (Number)
        self.unitOfMeasure = None  # (UnitOfMeasureReference)
        self.serializedFlag = None  # (Boolean)
        self.serialNumber = None  # (String)
        self.shipmentMethod = None  # (ShipmentMethodReference)
        self.packingSlip = None  # (String)
        self.ticket = None  # (TicketReference)
        self.project = None  # (ProjectReference)
        self.phase = None  # (ProjectPhaseReference)
        self.expenseClass = None  # (Enum)
        self.expenseType = None  # (ExpenseTypeReference)
        self.timeEntry = None  # (TimeEntryReference)
        self.activity = None  # (ActivityReference)
        self.segment1 = None  # (String)
        self.segment2 = None  # (String)
        self.segment3 = None  # (String)
        self.segment4 = None  # (String)
        self.segment5 = None  # (String)
        self.segment6 = None  # (String)
        self.segment7 = None  # (String)
        self.segment8 = None  # (String)
        self.segment9 = None  # (String)
        self.segment10 = None  # (String)
        self.avalaraTaxFlag = None  # (Boolean)
        self.itemTaxableFlag = None  # (Boolean)
        self.taxCode = None  # (TaxCodeReference)
        self.stateTaxFlag = None  # (Boolean)
        self.stateTaxXref = None  # (String)
        self.stateTaxAmount = None  # (Number)
        self.countyTaxFlag = None  # (Boolean)
        self.countyTaxXref = None  # (String)
        self.countyTaxAmount = None  # (Number)
        self.cityTaxFlag = None  # (Boolean)
        self.cityTaxXref = None  # (String)
        self.cityTaxAmount = None  # (Number)
        self.countryTaxFlag = None  # (Boolean)
        self.countryTaxXref = None  # (String)
        self.countryTaxAmount = None  # (Number)
        self.compositeTaxFlag = None  # (Boolean)
        self.compositeTaxXref = None  # (String)
        self.compositeTaxAmount = None  # (Number)
        self.taxTotal = None  # (Number)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
