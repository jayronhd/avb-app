SELECT TOP(1)
(SELECT TOP(1) _Average FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE _Name = 'STD01 RFA' ORDER BY _TimeStamp DESC) AS STD01_RFA,
(SELECT TOP(1) _Average FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE _Name = 'STD02 RFA' ORDER BY _TimeStamp DESC) AS STD02_RFA,
(SELECT TOP(1) _Average FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE _Name = 'STD03 RFA' ORDER BY _TimeStamp DESC) AS STD03_RFA,
(SELECT TOP(1) _Average FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE _Name = 'STD04 RFA' ORDER BY _TimeStamp DESC) AS STD04_RFA,
(SELECT TOP(1) _Average FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE _Name = 'STD05 RFA' ORDER BY _TimeStamp DESC) AS STD05_RFA,
(SELECT TOP(1) _Average FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE _Name = 'STD06 RFA' ORDER BY _TimeStamp DESC) AS STD06_RFA,
(SELECT TOP(1) _Average FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE _Name = 'STD07 RFA' ORDER BY _TimeStamp DESC) AS STD07_RFA,
(SELECT TOP(1) _Average FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE _Name = 'STD08 RFA' ORDER BY _TimeStamp DESC) AS STD08_RFA,
(SELECT TOP(1) _Average FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE _Name = 'STD09 RFA' ORDER BY _TimeStamp DESC) AS STD09_RFA,
(SELECT TOP(1) _Average FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE _Name = 'STD10 RFA' ORDER BY _TimeStamp DESC) AS STD10_RFA,
(SELECT TOP(1) _Average FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE _Name = 'STD11 RFA' ORDER BY _TimeStamp DESC) AS STD11_RFA,
(SELECT TOP(1) _Average FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE _Name = 'STD12 RFA' ORDER BY _TimeStamp DESC) AS STD12_RFA,
(SELECT TOP(1) _Average FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE _Name = 'STD13 RFA' ORDER BY _TimeStamp DESC) AS STD13_RFA,
(SELECT TOP(1) _Average FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE _Name = 'STD14 RFA' ORDER BY _TimeStamp DESC) AS STD14_RFA,
(SELECT TOP(1) _Average FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE _Name = 'STD15 RFA' ORDER BY _TimeStamp DESC) AS STD15_RFA,
(SELECT TOP(1) _Average FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE _Name = 'STD16 RFA' ORDER BY _TimeStamp DESC) AS STD16_RFA,
(SELECT TOP(1) _Average FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE _Name = 'STD17 RFA' ORDER BY _TimeStamp DESC) AS STD17_RFA,
(SELECT TOP(1) _Average FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE _Name = 'STD18 RFA' ORDER BY _TimeStamp DESC) AS STD18_RFA
FROM [iba_db].[dbo].[VIEW_IBA_DAT] WHERE YEAR(_TimeStamp) = YEAR(GETDATE()) AND MONTH(_TimeStamp) = MONTH(GETDATE()) AND DAY(_TimeStamp) = DAY(GETDATE());
