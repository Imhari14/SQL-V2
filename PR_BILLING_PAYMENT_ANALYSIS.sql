CREATE PROCEDURE PR_BILLING_PAYMENT_ANALYSIS
(
    IN IP_FKDAT_FROM DATE,
    IN IP_FKDAT_TO DATE,
    IN IP_BUKRS VARCHAR(4)
)
LANGUAGE SQL
AS
BEGIN
    /*
    Purpose: Analyze billing and payment processes including clearing status
    Tables: VBRK (Billing Document Header)
           VBRP (Billing Document Items)
           BSID (Customer Line Items)
           BSAD (Cleared Customer Items)
           KONV (Pricing Conditions)
    */
    
    TRUNCATE TABLE CT_BILLING_PAYMENT_ANALYSIS;
    
    INSERT INTO CT_BILLING_PAYMENT_ANALYSIS
    (
        BILLING_DOC,
        BILLING_TYPE,
        BILLING_DATE,
        ORDER_REF,
        CUSTOMER,
        NET_VALUE,
        PAYMENT_TERMS,
        CLEARING_DATE,
        CLEARING_DOC,
        PAYMENT_DELAY,
        DISCOUNT_AMOUNT,
        PARTITION_ID,
        CREATED_AT
    )
    SELECT 
        VBRK.VBELN as BILLING_DOC,
        VBRK.FKART as BILLING_TYPE,
        VBRK.FKDAT as BILLING_DATE,
        VBRK.VGBEL as ORDER_REF,
        VBRK.KUNAG as CUSTOMER,
        SUM(VBRP.NETWR) as NET_VALUE,
        VBRK.ZTERM as PAYMENT_TERMS,
        BSAD.AUGDT as CLEARING_DATE,
        BSAD.AUGBL as CLEARING_DOC,
        CASE 
            WHEN BSAD.AUGDT IS NOT NULL 
            THEN DATEDIFF(DAY, VBRK.FKDAT, BSAD.AUGDT)
            ELSE NULL 
        END as PAYMENT_DELAY,
        SUM(
            CASE 
                WHEN KONV.KSCHL IN ('RA00', 'RA01') 
                THEN KONV.KWERT
                ELSE 0 
            END
        ) as DISCOUNT_AMOUNT,
        1 as PARTITION_ID,
        CURRENT_TIMESTAMP as CREATED_AT
    FROM VBRK
    INNER JOIN VBRP
        ON VBRK.MANDT = VBRP.MANDT
        AND VBRK.VBELN = VBRP.VBELN
    LEFT JOIN BSID
        ON VBRK.MANDT = BSID.MANDT
        AND VBRK.VBELN = BSID.VBELN
    LEFT JOIN BSAD
        ON BSID.MANDT = BSAD.MANDT
        AND BSID.KUNNR = BSAD.KUNNR
        AND BSID.BELNR = BSAD.BELNR
    LEFT JOIN KONV
        ON VBRK.MANDT = KONV.MANDT
        AND VBRK.KNUMV = KONV.KNUMV
    WHERE VBRK.FKDAT BETWEEN :IP_FKDAT_FROM AND :IP_FKDAT_TO
    AND VBRK.BUKRS = :IP_BUKRS
    AND VBRK.FKART IN ('F2', 'G2', 'S1')
    GROUP BY 
        VBRK.VBELN,
        VBRK.FKART,
        VBRK.FKDAT,
        VBRK.VGBEL,
        VBRK.KUNAG,
        VBRK.ZTERM,
        BSAD.AUGDT,
        BSAD.AUGBL;

    -- Update payment performance statistics
    INSERT INTO CT_PAYMENT_STATISTICS
    (
        ANALYSIS_DATE,
        TOTAL_INVOICES,
        CLEARED_INVOICES,
        AVG_PAYMENT_DELAY,
        TOTAL_DISCOUNTS,
        CREATED_AT
    )
    SELECT 
        CURRENT_DATE,
        COUNT(DISTINCT BILLING_DOC),
        COUNT(DISTINCT CASE WHEN CLEARING_DATE IS NOT NULL THEN BILLING_DOC END),
        AVG(PAYMENT_DELAY),
        SUM(DISCOUNT_AMOUNT),
        CURRENT_TIMESTAMP
    FROM CT_BILLING_PAYMENT_ANALYSIS;
END;
