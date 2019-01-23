CREATE FUNCTION UscPLM.Initcap (@inStr VARCHAR(8000))
  RETURNS VARCHAR(8000)
  AS
  BEGIN
    DECLARE @outStr VARCHAR(8000) = LOWER(@inStr),
         @char CHAR(1), 
         @alphanum BIT = 0,
         @len INT = LEN(@inStr),
                 @pos INT = 1;        
-- Iterar entre todos los caracteres en la cadena de entrada
    WHILE @pos <= @len BEGIN
-- Obtener el siguiente caracter
      SET @char = SUBSTRING(@inStr, @pos, 1);
-- Si la posición del caracter es la 1ª, o el caracter previo no es alfanumérico
      -- convierte el caracter actual a mayúscula
      IF @pos = 1 OR @alphanum = 0
        SET @outStr = STUFF(@outStr, @pos, 1, UPPER(@char));
SET @pos = @pos + 1;
-- Define si el caracter actual es  non-alfanumérico
      IF ASCII(@char) <= 47 OR (ASCII(@char) BETWEEN 58 AND 64) OR
      (ASCII(@char) BETWEEN 91 AND 96) OR (ASCII(@char) BETWEEN 123 AND 126)
      SET @alphanum = 0;
      ELSE
      SET @alphanum = 1;
END
RETURN @outStr;         
  END
--  GO
-- Algunas pruebas ...
  SELECT UscPLM.Initcap('#estadoS uNIDOS dE aMÉRICA');
  SELECT UscPLM.Initcap(' estadoS uNIDOS dE aMÉRICA');
  SELECT UscPLM.Initcap('PAPA FRANCISCO');

