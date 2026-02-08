## Question

What is the difference between GMT and UTC?<br><br>

Please select 1 option<br><br>

A) GMT is a time zone, UTC is a worldwide time standard<br>
B) GMT and UTC are exactly identical and interchangeable<br>
C) UTC is only for astronomy, GMT is for global coordination<br>
D) GMT adjusts for DST, UTC does not

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>GMT (Greenwich Mean Time):</strong><br>
• A <strong>time zone</strong><br>
• Based on Greenwich Observatory<br>
• Historical term<br><br>

<strong>UTC (Coordinated Universal Time):</strong><br>
• A <strong>time standard</strong> used worldwide<br>
• Based on atomic clocks<br>
• More precise than GMT<br>
• International reference<br><br>

In practice, GMT and UTC are very close but <strong>technically different</strong>.<br><br>

<strong>B) is incorrect:</strong> Not exactly identical technically.<br>
<strong>C) is incorrect:</strong> UTC is the worldwide standard, not just for astronomy.<br>
<strong>D) is incorrect:</strong> Neither GMT nor UTC adjusts for DST.

## Question

What is a time zone in Java?<br><br>

Please select 1 option<br><br>

A) A fixed time offset from UTC<br>
B) A local time without geographical context<br>
C) A time display format<br>
D) A definition that includes a UTC offset, DST rules, and history

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

A <strong>time zone</strong> defines how an Instant (UTC) is displayed locally.<br><br>

It includes:<br>
• A <strong>UTC offset</strong><br>
• <strong>Daylight saving time (DST) rules</strong><br>
• A <strong>history</strong> of changes<br><br>

A time zone is intelligent and handles variations automatically.<br><br>

<strong>A) is incorrect:</strong> That's an offset, not a complete time zone.<br>
<strong>B) is incorrect:</strong> That's LocalDateTime.<br>
<strong>C) is incorrect:</strong> It's more than a display format.

## Question

What does ZoneId represent in Java?<br><br>

Please select 1 option<br><br>

A) A real geographical time zone that automatically handles DST<br>
B) A fixed time offset like +02:00<br>
C) A date and time format<br>
D) A class for handling only UTC

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>ZoneId</strong> represents a real (geographical) time zone.<br><br>

Examples:<br>
• Europe/Paris<br>
• America/New_York<br><br>

Automatically handles:<br>
• Daylight saving time (DST)<br>
• Historical changes<br><br>

<strong>Different from a fixed offset</strong> (+02:00).<br><br>

<strong>B) is incorrect:</strong> A fixed offset doesn't handle DST.<br>
<strong>C) and D) are incorrect:</strong> Wrong definition.

## Question

What does ZonedDateTime represent?<br><br>

Please select 1 option<br><br>

A) A date without time<br>
B) An absolute point in UTC time<br>
C) A local time without time zone<br>
D) Date + time + ZoneId (complete human representation)

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>ZonedDateTime</strong> represents:<br>
<strong>date + time + ZoneId</strong><br><br>

Characteristics:<br>
• The <strong>complete human representation</strong> of time<br>
• Based on <strong>ISO-8601</strong> calendar<br>
• <strong>Immutable</strong> and <strong>thread-safe</strong><br><br>

Example: 2025-02-04T15:30:00+01:00[Europe/Paris]<br><br>

<strong>A) is incorrect:</strong> Contains date AND time.<br>
<strong>B) is incorrect:</strong> That's Instant.<br>
<strong>C) is incorrect:</strong> That's LocalDateTime.

## Question

What is DST (Daylight Saving Time)?<br><br>

Please select 1 option<br><br>

A) A standardized date format<br>
B) A temporal encryption algorithm<br>
C) The transition between daylight saving time and standard time<br>
D) A time zone database

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>DST (Daylight Saving Time):</strong><br>
• Transition between daylight/standard time<br>
• Automatically managed by <strong>ZoneId</strong><br><br>

Important:<br>
• Fixed offsets do NOT handle DST<br>
• ZoneIds automatically handle DST<br><br>

<strong>A), B), D) are incorrect:</strong> Wrong definition.

## Question

What is the main difference between LocalDateTime and ZonedDateTime?<br><br>

Please select 1 option<br><br>

A) LocalDateTime is faster<br>
B) LocalDateTime has no time zone or DST, ZonedDateTime has both<br>
C) ZonedDateTime cannot represent future dates<br>
D) There is no difference

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Difference:</strong><br><br>

<strong>LocalDateTime:</strong><br>
• ❌ No time zone<br>
• ❌ No DST<br>
• = local time without context<br><br>

<strong>ZonedDateTime:</strong><br>
• ✅ Time zone (ZoneId)<br>
• ✅ DST automatically managed<br>
• = contextualized human time<br><br>

<strong>A) is incorrect:</strong> Performance is not the key difference.<br>
<strong>C) is incorrect:</strong> ZonedDateTime can represent any date.<br>
<strong>D) is incorrect:</strong> These are very different types.

## Question

What is the difference between an offset and a ZoneId?<br><br>

Please select 1 option<br><br>

A) An offset handles DST, a ZoneId does not<br>
B) They are two terms for the same thing<br>
C) An offset is fixed, a ZoneId is intelligent and handles DST<br>
D) A ZoneId is always in UTC

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Difference (major trap):</strong><br><br>

<strong>Offset:</strong><br>
• Example: +02:00<br>
• ❌ Does NOT handle DST<br>
• Fixed, static<br><br>

<strong>ZoneId:</strong><br>
• Example: Europe/Paris<br>
• ✅ Automatically handles DST<br>
• Intelligent, dynamic<br><br>

An offset is fixed, a zone is intelligent.<br><br>

<strong>A) is incorrect:</strong> It's the opposite.<br>
<strong>B) and D) are incorrect:</strong> Different concepts.

## Question

What relationship exists between Instant and ZonedDateTime?<br><br>

Please select 1 option<br><br>

A) They are two incompatible types<br>
B) A ZonedDateTime = an Instant + a ZoneId<br>
C) Instant is obsolete, use ZonedDateTime<br>
D) ZonedDateTime cannot be converted to Instant

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Fundamental relationship:</strong><br>
<strong>A ZonedDateTime = an Instant + a ZoneId</strong><br><br>

Consequences:<br>
• Same instant → different displays depending on zone<br>
• Conversion possible in both directions<br><br>

Example:<br>
Instant: 2025-02-04T14:30:00Z<br>
+ Europe/Paris → 2025-02-04T15:30:00+01:00[Europe/Paris]<br>
+ America/New_York → 2025-02-04T09:30:00-05:00[America/New_York]<br><br>

<strong>A), C), D) are incorrect:</strong> False understanding of the relationship.

## Question

What is "DST Gap" (non-existent hour)?<br><br>

Please select 1 option<br><br>

A) A programming error<br>
B) A bug in ZoneId<br>
C) An hour that exists twice<br>
D) An hour that doesn't exist during the spring DST transition

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>DST Gap (non-existent hour)</strong> occurs during the spring DST transition.<br><br>

Example (Europe/Paris):<br>
01:59 → 03:00<br><br>

An hour like <strong>02:30 doesn't exist</strong>.<br><br>

Java automatically adjusts to a valid hour.<br><br>

This is a critical problem to understand for the exam.<br><br>

<strong>A) and B) are incorrect:</strong> It's normal DST behavior.<br>
<strong>C) is incorrect:</strong> That's DST ambiguity, not gap.

## Question

What is "DST Ambiguity" (repeated hour)?<br><br>

Please select 1 option<br><br>

A) Two identical time zones<br>
B) The same local time that exists twice during the fall DST transition<br>
C) A Java calculation error<br>
D) An ambiguous date format

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>DST Ambiguity (repeated hour)</strong> occurs during the fall DST transition.<br><br>

Problem:<br>
• The same local time <strong>exists twice</strong><br>
• Java must choose an offset<br>
• <strong>Classic exam trap</strong><br><br>

Example:<br>
At 3 AM, clocks go back to 2 AM.<br>
So 2:30 exists twice that night.<br><br>

<strong>A), C), D) are incorrect:</strong> Wrong definition.

## Question

What is the correct conversion between time zones?<br><br>

Please select 1 option<br><br>

A) Keep local time but change zone<br>
B) Add offset manually<br>
C) Convert to String first then parse<br>
D) Change zone without changing instant (result: different time, same instant)

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>Correct conversion (same instant):</strong><br>
• Change zone <strong>without changing instant</strong><br>
• Result: different time, same instant<br><br>

Example:<br>
15:00 Europe/Paris → 09:00 America/New_York<br>
(same moment, different display)<br><br>

<strong>Classic error:</strong><br>
• Keep local time but change zone<br>
• This changes the instant (often wrong in business logic)<br><br>

<strong>A) is incorrect:</strong> That's the classic error.<br>
<strong>B) and C) are incorrect:</strong> Not the right approach.

## Question

What happens if you create a ZonedDateTime with a time in the DST gap?<br><br>

Please select 1 option<br><br>

A) An exception is thrown<br>
B) Java automatically adjusts to a valid time<br>
C) Creation fails silently<br>
D) The time remains exactly as requested

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

During a <strong>DST gap</strong> (non-existent hour):<br>
Java <strong>automatically adjusts</strong> to a valid time.<br><br>

Example:<br>
If you try to create 02:30 during the spring DST transition,<br>
Java will create 03:30 instead.<br><br>

No exception, <strong>automatic adjustment</strong>.<br><br>

<strong>A) is incorrect:</strong> No exception thrown.<br>
<strong>C) and D) are incorrect:</strong> Time is adjusted.

## Question

Which type should you use to represent an appointment in Paris on March 15, 2025 at 2:30 PM?<br><br>

Please select 1 option<br><br>

A) LocalDateTime<br>
B) Instant<br>
C) ZonedDateTime with Europe/Paris<br>
D) OffsetDateTime with +01:00

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

For a <strong>geographical appointment</strong>, use <strong>ZonedDateTime</strong> with the appropriate zone.<br><br>

Reasons:<br>
• The appointment has a <strong>geographical context</strong> (Paris)<br>
• Must handle <strong>DST</strong> automatically<br>
• Europe/Paris will adjust if DST changes<br><br>

<strong>A) is incorrect:</strong> No time zone = ambiguous.<br>
<strong>B) is incorrect:</strong> Instant is for absolute points, not human appointments.<br>
<strong>D) is incorrect:</strong> A fixed offset doesn't handle DST.

## Question

How do you correctly convert a ZonedDateTime from Paris to New York?<br><br>

Please select 1 option<br><br>

A) zdtParis.withZoneSameInstant(ZoneId.of("America/New_York"))<br>
B) zdtParis.plusHours(-6)<br>
C) zdtParis.withZoneSameLocal(ZoneId.of("America/New_York"))<br>
D) Create a new ZonedDateTime with the same values

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

The correct method is <strong>withZoneSameInstant()</strong>.<br><br>

This method:<br>
• Keeps the <strong>same instant</strong><br>
• Changes the display according to the new zone<br>
• Result: different time, same instant<br><br>

<strong>C) is incorrect:</strong> withZoneSameLocal() keeps local time but changes instant (classic error).<br>
<strong>B) is incorrect:</strong> Imprecise manual calculation (and offset isn't always -6).<br>
<strong>D) is incorrect:</strong> Too complex and error-prone.

## Question

How do you create a ZonedDateTime for "now" in Paris?<br><br>

Please select 1 option<br><br>

A) new ZonedDateTime("Europe/Paris")<br>
B) ZonedDateTime.of("Europe/Paris")<br>
C) ZonedDateTime.now(ZoneId.of("Europe/Paris"))<br>
D) Instant.now().atZone("Europe/Paris")

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

The correct method is <strong>ZonedDateTime.now(ZoneId.of("Europe/Paris"))</strong>.<br><br>

This method:<br>
• Gets the current instant<br>
• Displays it in the specified zone<br><br>

<strong>A) is incorrect:</strong> No public constructor.<br>
<strong>B) is incorrect:</strong> of() requires complete date and time.<br>
<strong>D) is incorrect:</strong> Incorrect syntax (atZone takes a ZoneId, not a String).

## Question

What happens when converting ZonedDateTime to Instant?<br><br>

Please select 1 option<br><br>

A) You lose the time zone information but keep the exact point in time<br>
B) You lose the exact point in time<br>
C) Nothing changes, they are equivalent types<br>
D) The conversion is impossible

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

When converting <strong>ZonedDateTime → Instant</strong>:<br>
• You <strong>lose the time zone information</strong><br>
• You <strong>keep the exact point in time</strong><br><br>

Example:<br>
ZonedDateTime zdt = ... // 15:00+01:00[Europe/Paris]<br>
Instant instant = zdt.toInstant(); // 14:00:00Z (UTC)<br><br>

The moment is identical, but representation is in UTC without time zone.<br><br>

<strong>B), C), D) are incorrect:</strong> Misunderstanding of the conversion.

## Question

What is the result of this code?<br><br>

```java
ZonedDateTime zdt = ZonedDateTime.of(
    2024, 1, 15, 10, 30, 0, 0,
    ZoneId.of("Europe/Paris")
);
Instant instant = zdt.toInstant();
System.out.println(instant);
```
<br><br>

Please select 1 option<br><br>

A) 2024-01-15T10:30:00Z<br>
B) 2024-01-15T09:30:00Z<br>
C) 2024-01-15T11:30:00Z<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Conversion ZonedDateTime → Instant:</strong><br>
• Europe/Paris in January = UTC+1<br>
• 10:30 Paris time = 09:30 UTC<br>
• toInstant() converts to UTC<br><br>

Result: <strong>2024-01-15T09:30:00Z</strong><br><br>

<strong>A) is incorrect:</strong> Forgot to apply timezone offset.<br>
<strong>C) is incorrect:</strong> Wrong direction of offset.<br>
<strong>D) is incorrect:</strong> Code compiles fine.

## Question

What will this code print?<br><br>

```java
ZonedDateTime zdt1 = ZonedDateTime.of(
    2024, 1, 15, 14, 0, 0, 0,
    ZoneId.of("Europe/Paris")
);
ZonedDateTime zdt2 = zdt1.withZoneSameInstant(ZoneId.of("America/New_York"));
System.out.println(zdt1.getHour());
System.out.println(zdt2.getHour());
```
<br><br>

Please select 1 option<br><br>

A) 14<br>
8<br><br>

B) 14<br>
14<br><br>

C) 8<br>
14<br><br>

D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>withZoneSameInstant():</strong><br>
• Keeps the <strong>same instant</strong><br>
• Changes display to new zone<br><br>

Calculation:<br>
• Paris: 14:00 (UTC+1 in January)<br>
• New York: 08:00 (UTC-5 in January)<br>
• Time difference: 6 hours<br><br>

Output:<br>
14 (Paris time)<br>
8 (New York time)<br><br>

<strong>B), C), D) are incorrect:</strong> Wrong conversion or understanding.

## Question

What is the result of this code?<br><br>

```java
Instant instant1 = Instant.parse("2024-01-15T10:00:00Z");
Instant instant2 = Instant.parse("2024-01-15T11:00:00+01:00");
System.out.println(instant1.equals(instant2));
```
<br><br>

Please select 1 option<br><br>

A) true<br>
B) false<br>
C) Compilation error<br>
D) Runtime exception

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>Same instant, different representations:</strong><br>
• instant1: 10:00 UTC (Z = UTC)<br>
• instant2: 11:00 with offset +01:00 = 10:00 UTC<br><br>

Both represent the <strong>same absolute point in time</strong>.<br><br>

Result: <strong>true</strong><br><br>

<strong>B) is incorrect:</strong> Same instant in UTC.<br>
<strong>C) and D) are incorrect:</strong> Code runs without error.

## Question

Which of the following are true about ZoneId in Java?<br><br>

Please select all that apply<br><br>

A) ZoneId represents a geographical time zone<br>
B) ZoneId automatically handles DST transitions<br>
C) ZoneId is identical to a fixed offset like +02:00<br>
D) ZoneId can be created with ZoneId.of("Europe/Paris")<br>
E) ZoneId only works with Instant

## Réponse

<strong>Réponses correctes :</strong> A), B), D)<br><br>

<strong>A) ✅ Correct:</strong> ZoneId represents a real geographical time zone with full DST history.<br>
<strong>B) ✅ Correct:</strong> Unlike a fixed offset, ZoneId automatically adjusts for DST changes.<br>
<strong>D) ✅ Correct:</strong> ZoneId.of("Europe/Paris") is the standard way to create a named zone.<br><br>

<strong>C) ❌ Incorrect:</strong> A fixed offset (+02:00) never changes; ZoneId is intelligent and dynamic.<br>
<strong>E) ❌ Incorrect:</strong> ZoneId is used with ZonedDateTime, and also indirectly via atZone() on Instant.

## Question

Which of the following statements about DST (Daylight Saving Time) are correct?<br><br>

Please select all that apply<br><br>

A) During a DST gap, Java throws an exception<br>
B) During a DST ambiguity, the same local time can occur twice<br>
C) Fixed offsets like +02:00 automatically handle DST<br>
D) ZonedDateTime automatically adjusts for DST transitions<br>
E) DST gap occurs during the spring transition

## Réponse

<strong>Réponses correctes :</strong> B), D), E)<br><br>

<strong>B) ✅ Correct:</strong> During the fall transition, clocks go back, so one hour repeats — this is DST ambiguity.<br>
<strong>D) ✅ Correct:</strong> ZonedDateTime with a named ZoneId automatically handles DST.<br>
<strong>E) ✅ Correct:</strong> Clocks spring forward in spring, skipping an hour (DST gap).<br><br>

<strong>A) ❌ Incorrect:</strong> Java does NOT throw an exception; it automatically adjusts to a valid time.<br>
<strong>C) ❌ Incorrect:</strong> Fixed offsets are static and do not adapt to DST — only named ZoneIds do.

## Question

Which of the following correctly describe the relationship between Instant and ZonedDateTime?<br><br>

Please select all that apply<br><br>

A) ZonedDateTime = Instant + ZoneId<br>
B) Instant is always expressed in UTC<br>
C) Converting ZonedDateTime to Instant loses the time zone but preserves the moment<br>
D) The same Instant always displays the same time in all time zones<br>
E) You can convert an Instant to a ZonedDateTime using atZone()

## Réponse

<strong>Réponses correctes :</strong> A), B), C), E)<br><br>

<strong>A) ✅ Correct:</strong> ZonedDateTime is conceptually an Instant plus a ZoneId for display.<br>
<strong>B) ✅ Correct:</strong> Instant represents a point on the UTC timeline.<br>
<strong>C) ✅ Correct:</strong> toInstant() preserves the exact moment but drops zone information.<br>
<strong>E) ✅ Correct:</strong> instant.atZone(ZoneId.of("Europe/Paris")) is the correct conversion.<br><br>

<strong>D) ❌ Incorrect:</strong> The same Instant displays different local times depending on the time zone.
