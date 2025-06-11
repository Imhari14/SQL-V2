CREATE PROCEDURE PR_BSEG_ACTIVITY_LOAD
(
    IN IP_BUDAT_FROM DATE,
    IN IP_BUDAT_TO DATE,
    IN IP_BUKRS VARCHAR(4)
)
LANGUAGE SQL
AS
BEGIN
    /*
    Purpose: Extract BSEG activities for OTC analysis
    Tables: BSEG (FI Document Line Items)
    */
    
    TRUNCATE TABLE CT_BSEG_DELTA_ACTIVITIES;
    
    INSERT INTO CT_BSEG_DELTA_ACTIVITIES
    (
        MANDT,
        BUKRS,
        BELNR,
        GJAHR,
        BUZEI,
        BUDAT,
        BLART,
        TCODE,
        SHKZG,
        WRBTR,
        PARTITION_ID,
        CREATED_AT
    )
    SELECT 
        MANDT,
        BUKRS,
        BELNR,
        GJAHR,
        BUZEI,
        BUDAT,
        BLART,
        TCODE,
        SHKZG,
        WRBTR,
        1 as PARTITION_ID,
        CURRENT_TIMESTAMP as CREATED_AT
    FROM BSEG
    WHERE BUDAT BETWEEN :IP_BUDAT_FROM AND :IP_BUDAT_TO
    AND BUKRS = :IP_BUKRS
    AND BLART IN ('SA', 'KR', 'DR');
END;
