from sqlmodel import Field, SQLModel


class AddressBase(SQLModel):
    name: str
    description: str


class Address(AddressBase, table=True):
    id: int = Field(default=None, primary_key=True)


class AddressCreate(AddressBase):
    pass
