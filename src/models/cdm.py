from pydantic import BaseModel
from datetime import datetime, date

class CDM(BaseModel):
    ccsds_cdm_vers: float
    creation_date: datetime
    originator: str
    message_id: int
    tca: datetime
    miss_distance: int
    object_designator: int
    catalog_name: str
    object_name: str
    international_designator: str
    ephemeris_name: str
    covariance_method: str
    maneuverable: str
    ref_frame: str
    x: float
    y: float
    z: float
    x_dot: float
    y_dot: float
    z_dot: float
    cr_r: float
    ct_r: float
    ct_t: float
    cn_r: float
    cn_t: float
    cn_n: float
    crdot_r: float
    crdot_t: float
    crdot_n: float
