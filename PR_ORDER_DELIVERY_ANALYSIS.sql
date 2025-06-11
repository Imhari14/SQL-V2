CREATE PROCEDURE PR_ORDER_DELIVERY_ANALYSIS
(
    IN IP_ERDAT_FROM DATE,
    IN IP_ERDAT_TO DATE,
    IN IP_VKORG VARCHAR(4)
)
LANGUAGE SQL
AS
BEGIN
    /*
    Purpose: Analyze order-to-delivery process including status tracking
    Tables: VBAK (Sales Document Header)
           VBAP (Sales Document Items)
           LIKP (Delivery Header)
           LIPS (Delivery Items)
           VBUK (Sales Document Status)
    */
    
    TRUNCATE TABLE CT_ORDER_DELIVERY_ANALYSIS;
    
    INSERT INTO CT_ORDER_DELIVERY_ANALYSIS
    (
        ORDER_NUM,
        ORDER_TYPE,
        ORDER_DATE,
        DELIVERY_NUM,
        DELIVERY_DATE,
        MATERIAL,
        QUANTITY,
        ORDER_STATUS,
        DELIVERY_STATUS,
        TOTAL_VALUE,
        PROCESS_DURATION,
        PARTITION_ID,
        CREATED_AT
    )
    SELECT 
        VBAK.VBELN as ORDER_NUM,
        VBAK.AUART as ORDER_TYPE,
        VBAK.ERDAT as ORDER_DATE,
        LIKP.VBELN as DELIVERY_NUM,
        LIKP.WADAT as DELIVERY_DATE,
        VBAP.MATNR as MATERIAL,
        LIPS.LFIMG as QUANTITY,
        CASE 
            WHEN VBUK.ABSTK = 'C' THEN 'Completed'
            WHEN VBUK.GBSTK = 'A' THEN 'Released'
            WHEN VBUK.GBSTK = 'B' THEN 'Partially Processed'
            ELSE 'In Process'
        END as ORDER_STATUS,
        CASE 
            WHEN LIKP.WBSTK = '4' THEN 'Picked'
            WHEN LIKP.WBSTK = 'A' THEN 'Posted'
            ELSE 'Open'
        END as DELIVERY_STATUS,
        SUM(VBAP.NETWR) as TOTAL_VALUE,
        DATEDIFF(DAY, VBAK.ERDAT, COALESCE(LIKP.WADAT, CURRENT_DATE)) as PROCESS_DURATION,
        1 as PARTITION_ID,
        CURRENT_TIMESTAMP as CREATED_AT
    FROM VBAK
    INNER JOIN VBAP 
        ON VBAK.MANDT = VBAP.MANDT
        AND VBAK.VBELN = VBAP.VBELN
    INNER JOIN VBUK
        ON VBAK.MANDT = VBUK.MANDT
        AND VBAK.VBELN = VBUK.VBELN
    LEFT JOIN LIPS
        ON VBAP.MANDT = LIPS.MANDT
        AND VBAP.VBELN = LIPS.VGBEL
        AND VBAP.POSNR = LIPS.VGPOS
    LEFT JOIN LIKP
        ON LIPS.MANDT = LIKP.MANDT
        AND LIPS.VBELN = LIKP.VBELN
    WHERE VBAK.ERDAT BETWEEN :IP_ERDAT_FROM AND :IP_ERDAT_TO
    AND VBAK.VKORG = :IP_VKORG
    AND VBAK.AUART IN ('OR', 'TA', 'ZOR')
    GROUP BY 
        VBAK.VBELN,
        VBAK.AUART,
        VBAK.ERDAT,
        LIKP.VBELN,
        LIKP.WADAT,
        VBAP.MATNR,
        LIPS.LFIMG,
        VBUK.ABSTK,
        VBUK.GBSTK,
        LIKP.WBSTK;
        
    -- Update statistics for process monitoring
    INSERT INTO CT_PROCESS_STATISTICS
    (
        PROCESS_DATE,
        TOTAL_ORDERS,
        COMPLETED_ORDERS,
        AVG_DURATION,
        CREATED_AT
    )
    SELECT 
        CURRENT_DATE,
        COUNT(DISTINCT ORDER_NUM),
        COUNT(DISTINCT CASE WHEN ORDER_STATUS = 'Completed' THEN ORDER_NUM END),
        AVG(PROCESS_DURATION),
        CURRENT_TIMESTAMP
    FROM CT_ORDER_DELIVERY_ANALYSIS;
END;
