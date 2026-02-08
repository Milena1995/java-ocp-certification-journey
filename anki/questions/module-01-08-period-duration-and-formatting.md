## Question

How do you correctly parse a String date with SimpleDateFormat?<br><br>

Please select 1 option<br><br>

A) Date date = Date.parse("yyyy-MM-dd", "2023-10-15");<br>
B) Date date = SimpleDateFormat.parse("yyyy-MM-dd", "2023-10-15");<br>
C) Date date = new SimpleDateFormat("yyyy-MM-dd").parse("2023-10-15");<br>
D) Date date = new Date("2023-10-15").format("yyyy-MM-dd");

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

The correct syntax is:<br>
<strong>Date date = new SimpleDateFormat("yyyy-MM-dd").parse("2023-10-15");</strong><br><br>

Steps:<br>
1. Create a SimpleDateFormat with the pattern<br>
2. Call parse() with the String<br><br>

Note:<br>
• This is the old API<br>
• In modern code, use DateTimeFormatter with java.time<br><br>

<strong>A), B), D) are incorrect:</strong> Incorrect syntax.

## Question

How does java.time.Period differ from Duration?<br><br>

Please select 1 option<br><br>

A) Period can only be used to convert time zones<br>
B) Period is always in UTC, Duration is local<br>
C) Duration can store future timestamps, Period cannot<br>
D) Period represents date-based differences (years, months, days), Duration represents time-based differences (hours, minutes, seconds)

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>Fundamental difference:</strong><br><br>

<strong>Period:</strong><br>
• Human-scale<br>
• Based on: <strong>years, months, days</strong><br>
• Calendar-dependent<br>
• Used with LocalDate<br><br>

<strong>Duration:</strong><br>
• Machine-scale<br>
• Based on: <strong>hours, minutes, seconds, nanoseconds</strong><br>
• Exact measurement<br>
• Used with Instant, LocalTime<br><br>

<strong>A), B), C) are incorrect:</strong> Misunderstanding of concepts.

## Question

In the old API, why is SimpleDateFormat NOT thread-safe?<br><br>

Please select 1 option<br><br>

A) Because it uses too much memory<br>
B) Because it is mutable and can be modified during use<br>
C) Because it does not support multithreading<br>
D) Because it is too slow

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>SimpleDateFormat is NOT thread-safe</strong> because it is <strong>mutable</strong>.<br><br>

Problem:<br>
• Modifiable internal state<br>
• Sharing between threads → unpredictable behavior<br>
• Possible data corruption<br><br>

Solutions with old API:<br>
• Create one instance per thread<br>
• Synchronize access<br>
• Use ThreadLocal<br><br>

<strong>Modern solution:</strong><br>
Use <strong>DateTimeFormatter</strong> (immutable and thread-safe).<br><br>

<strong>A), C), D) are incorrect:</strong> Not the real reason.

## Question

How do you get the number of days between two LocalDate objects?<br><br>

Please select 1 option<br><br>

A) ChronoUnit.DAYS.between(date1, date2);<br>
B) date1.minus(date2).getDays();<br>
C) Period.between(date1, date2).getTotalDays();<br>
D) Duration.between(date1, date2).toDays();

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

The correct method is <strong>ChronoUnit.DAYS.between(date1, date2)</strong>.<br><br>

Returns a <strong>long</strong> representing the number of days.<br><br>

Example:<br>
LocalDate d1 = LocalDate.of(2024, 1, 1);<br>
LocalDate d2 = LocalDate.of(2024, 1, 15);<br>
long days = ChronoUnit.DAYS.between(d1, d2); // 14<br><br>

<strong>B) is incorrect:</strong> minus() returns a LocalDate, not a duration.<br>
<strong>C) is incorrect:</strong> getTotalDays() doesn't exist (Period has getDays() but not total).<br>
<strong>D) is incorrect:</strong> Duration.between() doesn't work with LocalDate.

## Question

What does Period.between(LocalDate.of(2024, 1, 15), LocalDate.of(2024, 3, 10)) return?<br><br>

Please select 1 option<br><br>

A) P55D (55 days)<br>
B) P1M25D (1 month and 25 days)<br>
C) P2M (2 months)<br>
D) P1M26D (1 month and 26 days)

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Period.between()</strong> calculates the difference in <strong>years, months, and days</strong>.<br><br>

Calculation:<br>
• From January 15 to February 15 = 1 month<br>
• From February 15 to March 10 = 25 days<br>
• Total: <strong>P1M25D</strong> (1 month, 25 days)<br><br>

ISO format: P[years]Y[months]M[days]D<br><br>

Important: Period uses the calendar, not a total number of days.<br><br>

<strong>A), C), D) are incorrect:</strong> Wrong calculation.

## Question

What is the best practice for storing a reusable DateTimeFormatter?<br><br>

Please select 1 option<br><br>

A) Instantiate it in a synchronized block<br>
B) Create it each time it's used<br>
C) Declare it as a static final constant<br>
D) Use ThreadLocal

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Best practice:</strong> Declare as a <strong>static final constant</strong>.<br><br>

Example:<br>
private static final DateTimeFormatter FORMATTER = <br>
    DateTimeFormatter.ofPattern("dd/MM/yyyy");<br><br>

Reasons:<br>
• DateTimeFormatter is <strong>immutable</strong><br>
• <strong>Thread-safe</strong><br>
• Can be reused everywhere<br>
• Optimal performance<br><br>

<strong>B) is incorrect:</strong> Wasteful of resources.<br>
<strong>A) and D) are incorrect:</strong> Unnecessary since already thread-safe.

## Question

Which method formats a LocalDate to a custom String?<br><br>

Please select 1 option<br><br>

A) localDate.toString("dd/MM/yyyy");<br>
B) localDate.format(DateTimeFormatter.ofPattern("dd/MM/yyyy"));<br>
C) DateTimeFormatter.format(localDate, "dd/MM/yyyy");<br>
D) String.format(localDate, "dd/MM/yyyy");

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

The correct method is:<br>
<strong>localDate.format(DateTimeFormatter.ofPattern("dd/MM/yyyy"))</strong><br><br>

Example:<br>
LocalDate date = LocalDate.of(2024, 1, 15);<br>
String formatted = date.format(DateTimeFormatter.ofPattern("dd/MM/yyyy"));<br>
// Result: "15/01/2024"<br><br>

Or with a reusable formatter:<br>
private static final DateTimeFormatter FMT = DateTimeFormatter.ofPattern("dd/MM/yyyy");<br>
String formatted = date.format(FMT);<br><br>

<strong>A), C), D) are incorrect:</strong> Incorrect syntax.

## Question

What is ChronoUnit?<br><br>

Please select 1 option<br><br>

A) An interface for durations<br>
B) A date formatter<br>
C) A class for creating dates<br>
D) An enum representing time units

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>ChronoUnit</strong> is an <strong>enum</strong> representing time units.<br><br>

Examples:<br>
• ChronoUnit.DAYS<br>
• ChronoUnit.HOURS<br>
• ChronoUnit.MONTHS<br>
• ChronoUnit.YEARS<br><br>

Primarily used with <strong>between()</strong> to calculate differences.<br><br>

<strong>A), B), C) are incorrect:</strong> Wrong category.

## Question

Which statement about ChronoUnit.between() is correct?<br><br>

Please select 1 option<br><br>

A) Always returns a positive number<br>
B) Returns a long that can be negative<br>
C) Returns a Duration<br>
D) Throws an exception if the result is negative

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>ChronoUnit.between(a, b):</strong><br>
• Returns a <strong>long</strong><br>
• Can be <strong>positive, zero, or negative</strong><br><br>

Calculation: <strong>b - a</strong> on the timeline<br><br>

Negative means: date2 before date1<br><br>

Example:<br>
ChronoUnit.DAYS.between(date1, date2);<br>
// If result = -5 → date2 is 5 days before date1<br><br>

<strong>OCP trap:</strong> Negative = normal, not a bug.<br><br>

<strong>A), C), D) are incorrect:</strong> Misunderstanding.

## Question

Which type should you use to calculate a 30-second server timeout?<br><br>

Please select 1 option<br><br>

A) Period.ofSeconds(30)<br>
B) LocalDateTime.plusSeconds(30)<br>
C) ChronoUnit.SECONDS<br>
D) Duration.ofSeconds(30)

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

For an <strong>exact calculation</strong> (server timeout), use <strong>Duration</strong>.<br><br>

Example: Duration.ofSeconds(30)<br><br>

Reasons:<br>
• <strong>Machine-scale</strong> measurement<br>
• Exact precision in seconds/nanoseconds<br>
• Independent of calendar and DST<br><br>

<strong>A) is incorrect:</strong> Period doesn't have ofSeconds() method.<br>
<strong>B) is incorrect:</strong> LocalDateTime is not a duration.<br>
<strong>C) is incorrect:</strong> ChronoUnit is a unit, not a duration.

## Question

Which type should you use to add 1 month to a customer subscription?<br><br>

Please select 1 option<br><br>

A) Period.ofMonths(1)<br>
B) Duration.ofDays(30)<br>
C) LocalDate.plusDays(30)<br>
D) ChronoUnit.MONTHS

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

For a <strong>business rule</strong> (subscription + 1 month), use <strong>Period</strong>.<br><br>

Example: Period.ofMonths(1)<br><br>

Reasons:<br>
• <strong>Human-scale</strong> measurement<br>
• Respects calendar (months of different lengths)<br>
• Correctly handles leap years<br><br>

<strong>B) is incorrect:</strong> 1 month ≠ 30 days (February = 28/29 days).<br>
<strong>C) is incorrect:</strong> Adds directly, doesn't represent a reusable duration.<br>
<strong>D) is incorrect:</strong> It's a unit, not a period.

## Question

What does Duration.ofDays(1) mean?<br><br>

Please select 1 option<br><br>

A) A day that adapts to DST<br>
B) A human calendar day<br>
C) Exactly 24 hours (86400 seconds)<br>
D) A day in the local time zone

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Duration.ofDays(1)</strong> means <strong>exactly 24 hours</strong> (86400 seconds).<br><br>

Important:<br>
• <strong>Not a human day</strong><br>
• <strong>Not affected by DST</strong><br>
• Machine-scale, exact measurement<br><br>

<strong>OCP trap:</strong> Duration.ofDays(1) ≠ calendar day<br><br>

<strong>B) is incorrect:</strong> For a calendar day, use Period.ofDays(1).<br>
<strong>A) and D) are incorrect:</strong> Duration ignores DST and time zones.

## Question

Which date format is valid in ISO-8601 by default in Java?<br><br>

Please select 1 option<br><br>

A) 15/01/2024<br>
B) 2024-01-15<br>
C) 2024/01/15<br>
D) 2024-1-5

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Java uses <strong>strict ISO-8601</strong> by default.<br><br>

<strong>Valid examples:</strong><br>
• 2024-01-15<br>
• 2024-01-15T14:30<br>
• 2024-01-15T14:30Z<br><br>

<strong>Invalid examples:</strong><br>
• ❌ 2024-1-5 (missing zeros)<br>
• ❌ 15/01/2024 (slashes)<br>
• ❌ 2024/01/15 (slashes)<br><br>

Java never guesses, never corrects.<br><br>

<strong>A), C), D) are incorrect:</strong> Non-ISO formats.

## Question

What is the role of DateTimeFormatter?<br><br>

Please select 1 option<br><br>

A) Only validate dates<br>
B) Create date/time objects<br>
C) Calculate durations<br>
D) Convert object ↔ String with custom formats

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>DateTimeFormatter</strong> allows converting:<br>
• Object → String (<strong>format</strong>)<br>
• String → Object (<strong>parse</strong>)<br><br>

Advantages:<br>
• Allows non-ISO formats<br>
• <strong>Immutable</strong><br>
• <strong>Thread-safe</strong><br>
• Can be reused everywhere<br><br>

OCP best practice: one formatter = shared constant.<br><br>

<strong>A), B), C) are incorrect:</strong> Not the main role.

## Question

What is the difference between "MM" and "mm" in a DateTimeFormatter?<br><br>

Please select 1 option<br><br>

A) MM = minutes, mm = months<br>
B) MM = months, mm = minutes<br>
C) No difference<br>
D) Both represent months

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>CLASSIC OCP TRAP:</strong><br><br>

<strong>MM</strong> = <strong>months</strong> (Month)<br>
<strong>mm</strong> = <strong>minutes</strong> ❌ (beware of the trap)<br><br>

Java is <strong>strictly case-sensitive</strong>.<br><br>

Example:<br>
"yyyy-MM-dd" → year-month-day ✅<br>
"yyyy-mm-dd" → year-minutes-day ❌ (error)<br><br>

<strong>A), C), D) are incorrect:</strong> MM and mm are different.

## Question

What is the difference between "yyyy" and "YYYY" in a DateTimeFormatter?<br><br>

Please select 1 option<br><br>

A) No difference<br>
B) YYYY = calendar year, yyyy = week year<br>
C) yyyy = calendar year, YYYY = week year<br>
D) Both are identical in Java

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>VERY DANGEROUS OCP TRAP:</strong><br><br>

<strong>yyyy</strong> = <strong>calendar year</strong> ✅ (2024, 2025...)<br>
<strong>YYYY</strong> = <strong>week year</strong> ❌ (week year)<br><br>

<strong>Week year:</strong> can differ from calendar year at year start/end.<br><br>

Always use <strong>yyyy</strong> for normal dates.<br><br>

<strong>A), B), D) are incorrect:</strong> yyyy and YYYY are very different.

## Question

What is the difference between "dd" and "DD" in a DateTimeFormatter?<br><br>

Please select 1 option<br><br>

A) dd = day of month, DD = day of year<br>
B) DD = day of month, dd = day of year<br>
C) No difference<br>
D) Both are invalid

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>Difference:</strong><br><br>

<strong>dd</strong> = <strong>day of month</strong> (01-31)<br>
<strong>DD</strong> = <strong>day of year</strong> (001-365/366)<br><br>

Example:<br>
January 15, 2024:<br>
• dd = 15<br>
• DD = 015 (15th day of the year)<br><br>

<strong>B), C), D) are incorrect:</strong> Case sensitivity is critical.

## Question

What is the difference between "HH" and "hh" in a DateTimeFormatter?<br><br>

Please select 1 option<br><br>

A) HH = hour 1-12, hh = hour 0-23<br>
B) Both are for minutes<br>
C) No difference<br>
D) HH = hour 0-23, hh = hour 1-12 (AM/PM)

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>Difference:</strong><br><br>

<strong>HH</strong> = hour <strong>0-23</strong> (24h format)<br>
<strong>hh</strong> = hour <strong>1-12</strong> (AM/PM format)<br><br>

To use hh, you must also specify AM/PM with the pattern 'a'.<br><br>

Example:<br>
"HH:mm" → 14:30<br>
"hh:mm a" → 02:30 PM<br><br>

<strong>A), B), C) are incorrect:</strong> Wrong definition.

## Question

Is DateTimeFormatter thread-safe?<br><br>

Please select 1 option<br><br>

A) No, it must be synchronized<br>
B) Yes, because it is immutable<br>
C) Only if declared final<br>
D) It depends on the format used

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>DateTimeFormatter</strong> is:<br>
• <strong>Immutable</strong><br>
• <strong>Thread-safe</strong><br><br>

Consequences:<br>
• Can be reused everywhere<br>
• Can be shared between threads<br>
• No synchronization needed<br><br>

<strong>Best practice:</strong> Declare as static final constant.<br><br>

<strong>A), C), D) are incorrect:</strong> Thread-safe by nature.

## Question

Which default format does LocalDate use?<br><br>

Please select 1 option<br><br>

A) dd/MM/yyyy<br>
B) MM/dd/yyyy<br>
C) yyyy-MM-dd (ISO-8601)<br>
D) dd-MM-yyyy

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>LocalDate</strong> uses the <strong>ISO-8601</strong> format by default:<br>
<strong>yyyy-MM-dd</strong><br><br>

Characteristics:<br>
• Date without time<br>
• No time zone<br>
• International standard format<br><br>

Example: 2024-02-04<br><br>

<strong>A), B), D) are incorrect:</strong> Non-ISO formats.

## Question

For parsing "15/01/2024", which code is correct?<br><br>

Please select 1 option<br><br>

A) LocalDate.of(15, 1, 2024)<br>
B) new LocalDate("15/01/2024")<br>
C) LocalDate.parse("15/01/2024")<br>
D) LocalDate.parse("15/01/2024", DateTimeFormatter.ofPattern("dd/MM/yyyy"))

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

For a non-ISO format, you must <strong>create a DateTimeFormatter</strong>:<br><br>

LocalDate.parse("15/01/2024", DateTimeFormatter.ofPattern("dd/MM/yyyy"))<br><br>

<strong>C) is incorrect:</strong> ISO format expected by default.<br>
<strong>A) is incorrect:</strong> Parameter order: of(year, month, day).<br>
<strong>B) is incorrect:</strong> No String constructor.

## Question

Which of these statements is FALSE? (OCP trap)<br><br>

Please select 1 option<br><br>

A) Duration.ofDays(1) represents a human day that adapts to DST<br>
B) Period.ofMonths(1) represents 1 calendar month<br>
C) ChronoUnit.between() can return a negative number<br>
D) DateTimeFormatter is thread-safe

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>FALSE:</strong> Duration.ofDays(1) = human day → <strong>FALSE</strong><br><br>

<strong>Truth:</strong><br>
Duration.ofDays(1) = <strong>exactly 24 hours</strong><br>
• Not affected by DST<br>
• Machine-scale, not human-scale<br><br>

<strong>OCP traps to remember:</strong><br>
• ❌ Duration.ofDays(1) = human day<br>
• ❌ Period = seconds<br>
• ❌ MM = minutes<br>
• ❌ YYYY = calendar year<br><br>

<strong>B), C), D) are true.</strong>

## Question

If ChronoUnit.DAYS.between(date2, date1) returns -5, what does it mean?<br><br>

Please select 1 option<br><br>

A) There is an error in the code<br>
B) date1 is 5 days after date2<br>
C) date1 is 5 days before date2<br>
D) The dates are invalid

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>between(a, b)</strong> calculates: <strong>b - a</strong><br><br>

If between(date2, date1) = -5:<br>
• date1 - date2 = -5<br>
• So date1 is <strong>5 days before</strong> date2<br>
• Or: date2 is <strong>5 days after</strong> date1<br><br>

<strong>Negative result = normal</strong>, indicates temporal order.<br><br>

<strong>OCP trap:</strong> negative result ≠ bug<br><br>

<strong>A), B), D) are incorrect:</strong> Wrong interpretation of the sign.

## Question

What does ISO-8601 represent?<br><br>

Please select 1 option<br><br>

A) An encryption algorithm<br>
B) An international standard for representing dates and times<br>
C) A Java library for dates<br>
D) A particular time zone

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>ISO-8601</strong> is an <strong>international standard</strong> for representing dates and times.<br><br>

Typical format:<br>
2025-02-04T15:30:00+01:00[Europe/Paris]<br><br>

Java uses this standard for:<br>
• ZonedDateTime<br>
• LocalDateTime<br>
• Instant<br>
• All modern temporal types<br><br>

<strong>A), C), D) are incorrect:</strong> Wrong definition.

## Question

What will the following code print?<br><br>

```java
LocalDate d1 = LocalDate.of(2024, 3, 10);
LocalDate d2 = LocalDate.of(2024, 1, 15);
long days = ChronoUnit.DAYS.between(d1, d2);
System.out.println(days);
```
<br><br>

Please select 1 option<br><br>

A) 55<br>
B) -55<br>
C) 54<br>
D) -54

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>ChronoUnit.DAYS.between(d1, d2)</strong> calculates: <strong>d2 - d1</strong><br><br>

Calculation:<br>
• d1 = March 10, 2024<br>
• d2 = January 15, 2024<br>
• d2 is <strong>before</strong> d1<br>
• Result: <strong>-54 days</strong><br><br>

<strong>OCP trap:</strong> Negative result is normal, not an error.<br><br>

<strong>A), B), C) are incorrect:</strong> Wrong calculation or sign.

## Question

What will the following code print?<br><br>

```java
Period period = Period.between(
    LocalDate.of(2024, 1, 15),
    LocalDate.of(2024, 3, 10)
);
System.out.println(period.getDays());
```
<br><br>

Please select 1 option<br><br>

A) 55<br>
B) 54<br>
C) 25<br>
D) 24

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Period.getDays()</strong> returns ONLY the <strong>days component</strong>, not the total.<br><br>

Calculation:<br>
• From Jan 15 to Feb 15 = 1 month<br>
• From Feb 15 to Mar 10 = 25 days<br>
• Period = P1M25D<br>
• getDays() returns <strong>25</strong> (not 54)<br><br>

<strong>OCP trap:</strong> getDays() ≠ total days<br><br>

For total days, use: ChronoUnit.DAYS.between()<br><br>

<strong>A), B), D) are incorrect:</strong> Wrong understanding of getDays().

## Question

What will the following code print?<br><br>

```java
Duration d1 = Duration.ofDays(1);
Duration d2 = Duration.ofHours(24);
System.out.println(d1.equals(d2));
```
<br><br>

Please select 1 option<br><br>

A) true<br>
B) false<br>
C) Compilation error<br>
D) Runtime exception

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

Both durations represent <strong>exactly 24 hours (86400 seconds)</strong>.<br><br>

Calculation:<br>
• Duration.ofDays(1) = 24 hours = 86400 seconds<br>
• Duration.ofHours(24) = 24 hours = 86400 seconds<br>
• They are <strong>equal</strong><br><br>

Result: <strong>true</strong><br><br>

<strong>B), C), D) are incorrect:</strong> Durations are equivalent.

## Question

What will the following code print?<br><br>

```java
String pattern = "yyyy-MM-dd";
DateTimeFormatter formatter = DateTimeFormatter.ofPattern(pattern);
LocalDate date = LocalDate.parse("2024-13-15", formatter);
System.out.println(date);
```
<br><br>

Please select 1 option<br><br>

A) 2024-13-15<br>
B) 2025-01-15<br>
C) Compilation error<br>
D) DateTimeParseException at runtime

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>Invalid month:</strong><br>
• Month "13" doesn't exist<br>
• Valid months: 01-12<br>
• parse() throws <strong>DateTimeParseException</strong><br><br>

Java validates date components strictly.<br><br>

<strong>A) and B) are incorrect:</strong> Exception is thrown.<br>
<strong>C) is incorrect:</strong> Compiles fine, fails at runtime.

## Question

What will the following code print?<br><br>

```java
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/mm/yyyy");
LocalDate date = LocalDate.of(2024, 6, 15);
System.out.println(date.format(formatter));
```
<br><br>

Please select 1 option<br><br>

A) 15/06/2024<br>
B) 15/00/2024<br>
C) Compilation error<br>
D) Runtime exception

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>CRITICAL OCP TRAP:</strong><br>
• Pattern "mm" = <strong>minutes</strong> (not months!)<br>
• Pattern "MM" = months<br><br>

Result:<br>
• dd = 15 (day)<br>
• mm = 00 (minutes, no time so 00)<br>
• yyyy = 2024<br>
• Output: <strong>15/00/2024</strong><br><br>

Correct pattern: "dd/MM/yyyy"<br><br>

<strong>A) is incorrect:</strong> Would require MM not mm.<br>
<strong>C) and D) are incorrect:</strong> Code runs without error (but wrong output).

## Question

What will the following code print?<br><br>

```java
Period p1 = Period.ofMonths(1);
Period p2 = Period.ofDays(30);
System.out.println(p1.equals(p2));
```
<br><br>

Please select 1 option<br><br>

A) true<br>
B) false<br>
C) Compilation error<br>
D) Runtime exception

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Different representation:</strong><br>
• p1 = P1M (1 month)<br>
• p2 = P30D (30 days)<br><br>

Period doesn't convert between units:<br>
• 1 month ≠ 30 days (months vary: 28-31 days)<br>
• They are NOT equal<br><br>

Result: <strong>false</strong><br><br>

<strong>A) is incorrect:</strong> Different period components.<br>
<strong>C) and D) are incorrect:</strong> Code runs without error.

## Question

What is the output of this code?<br><br>

```java
Duration d = Duration.between(
    LocalTime.of(10, 0),
    LocalTime.of(14, 30)
);
System.out.println(d.toHours());
```
<br><br>

Please select 1 option<br><br>

A) 4<br>
B) 4.5<br>
C) 5<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>Duration.toHours():</strong><br>
• Converts to <strong>total hours</strong> (truncated)<br>
• Returns <strong>long</strong> (not double)<br><br>

Calculation:<br>
• From 10:00 to 14:30 = 4 hours 30 minutes<br>
• toHours() = <strong>4</strong> (truncates, doesn't round)<br><br>

Output: <strong>4</strong><br><br>

<strong>B) is incorrect:</strong> Returns long, not double.<br>
<strong>C) is incorrect:</strong> Truncates, doesn't round up.<br>
<strong>D) is incorrect:</strong> Code compiles fine.

## Question

Which of the following are true about Period in Java?<br><br>

Please select all that apply<br><br>

A) Period is based on years, months, and days<br>
B) Period.ofDays(1) always represents exactly 24 hours<br>
C) Period is used with LocalDate<br>
D) Period handles DST transitions<br>
E) Period is immutable

## Réponse

<strong>Réponses correctes :</strong> A), C), E)<br><br>

<strong>A) ✅ Correct:</strong> Period is composed of years, months, and days — human-scale.<br>
<strong>C) ✅ Correct:</strong> Period is designed to work with LocalDate for calendar arithmetic.<br>
<strong>E) ✅ Correct:</strong> Period is immutable like all java.time classes.<br><br>

<strong>B) ❌ Incorrect:</strong> Period.ofDays(1) is a calendar day and may span more or less than 24 hours due to DST — that is Duration's domain for exact 24-hour measurements.<br>
<strong>D) ❌ Incorrect:</strong> Period does not directly handle DST — it works at the calendar level.

## Question

Which of the following correctly describe DateTimeFormatter?<br><br>

Please select all that apply<br><br>

A) DateTimeFormatter is immutable<br>
B) DateTimeFormatter is thread-safe<br>
C) A new DateTimeFormatter instance must be created per thread<br>
D) DateTimeFormatter can both format and parse date-time objects<br>
E) DateTimeFormatter replaces Calendar in the old API

## Réponse

<strong>Réponses correctes :</strong> A), B), D)<br><br>

<strong>A) ✅ Correct:</strong> DateTimeFormatter is immutable — once created it cannot be changed.<br>
<strong>B) ✅ Correct:</strong> Because it is immutable, it is automatically thread-safe.<br>
<strong>D) ✅ Correct:</strong> It can format (object → String) and parse (String → object).<br><br>

<strong>C) ❌ Incorrect:</strong> Because it is thread-safe, one shared instance (e.g., static final) is sufficient.<br>
<strong>E) ❌ Incorrect:</strong> DateTimeFormatter is a formatter/parser; it does not replace Calendar — it replaces SimpleDateFormat.

## Question

Which of the following are valid ways to create a Duration?<br><br>

Please select all that apply<br><br>

A) Duration.ofSeconds(30)<br>
B) Duration.ofMonths(2)<br>
C) Duration.ofHours(4)<br>
D) Duration.between(LocalTime.of(10,0), LocalTime.of(14,0))<br>
E) new Duration(3600)

## Réponse

<strong>Réponses correctes :</strong> A), C), D)<br><br>

<strong>A) ✅ Correct:</strong> Duration.ofSeconds(30) is a valid factory method.<br>
<strong>C) ✅ Correct:</strong> Duration.ofHours(4) is a valid factory method.<br>
<strong>D) ✅ Correct:</strong> Duration.between() with two compatible temporal objects is valid.<br><br>

<strong>B) ❌ Incorrect:</strong> Duration has no ofMonths() method — months are calendar-based and belong to Period.<br>
<strong>E) ❌ Incorrect:</strong> Duration has no public constructor — use factory methods.
