# Style guide

## Contents

- [Reference hierarchy](#reference-hierarchy)
- [Photographs as loose topic guides](#photographs-as-loose-topic-guides)
- [Style in one sentence](#style-in-one-sentence)
- [Color structure](#color-structure)
- [Shape and anatomy](#shape-and-anatomy)
- [Movement and emotional construction](#movement-and-emotional-construction)
- [Depth, hair, and shared shapes](#depth-hair-and-shared-shapes)
- [Fused profiles and hidden symbolism](#fused-profiles-and-hidden-symbolism)
- [Surrounding details and subject meaning](#surrounding-details-and-subject-meaning)
- [Typography and image integration](#typography-and-image-integration)
- [Line and texture](#line-and-texture)
- [Prompt starters](#prompt-starters)
- [Diagnose drift before adding more texture](#diagnose-drift-before-adding-more-texture)

## Reference hierarchy

Select images with the [visual reference map](visual-reference-map.md), which
links each rule to a full source or detail crop and explains its limits.
The [family](../assets/source-family.png) and
[drummer](../assets/source-drummer.png) reproductions establish composition,
depth, shared-shape movement, color relationships, and subject-related setting.
Their [complete source](../assets/source-paintings.png) contains two separate
paintings, not a diptych. Use crops in context, not as interchangeable templates.

The [final-painting learning entries](../SKILL.md#learn-from-the-final-paintings)
link generated scenes in `../assets/final-paintings/` to specific lessons
and limitations. Use them for applications such as hand-to-instrument contact,
movement handoffs, and figure enclosure. They supplement the source artwork;
retaining them does not make every face or connection a style authority.
The pale skin and blue iris of the young drummer are a user-requested exception,
not a change to the default palette.

The approved generated reference for individual head shape, feature economy,
and finish is
`../assets/approved-head-studies.png`, a generated ten-head sheet supplied and
explicitly approved by the user. Preserve it unchanged.

`../assets/accepted-sideways-head.png` is the generated pose study the user
accepted as "much better" after restoring the lower cheek-jaw contour. It
establishes a readable whole sideways head overlapping a rising neck, without
the long line into the nose. It has one eye; a second eye is optional unless an
exact count is explicitly required. Do not treat the two-eye tests as accepted
visual references. Apply later
hair refinements to this pose: long hair for female characters by default,
falling downward without a cap across the image-top-facing head edge.

Earlier tall swan-neck attempts were rejected as inaccurate. Subsequent broad
sideways-head studies also failed by reading as animal muzzles. Neither approach
establishes the intended construction; rejected tests are not in the curated
reference set.

The source discussion concerned two separate paintings shown side by side,
not a diptych. The family painting supplied single-eye profiles, interlocking
figures, and a user-identified morphing couple/heart reading. The drummer
supplied a deeply bent head absorbed in playing, not animal-like skull anatomy.
These observations extend the vocabulary beyond the generated head studies.
Artist identity, materials, dimensions, and intended symbolism are unverified.

Rejected generations are not alternate references. They drifted in two main
directions: long animal-like drummer muzzles, and overly polished human portraits.
Other studies separated a couple into literal heart-shaped silhouettes instead
of letting their features morph.

## Photographs as loose topic guides

A subject photograph answers "what is this about?" It does not answer "what
exact shapes should be drawn?" Extract the subjects, their activity or
relationship, the general setting, and broad positions such as above/below,
beside, carrying, or leaning toward. The artwork references, not the photograph,
establish how those ideas become shapes.

Translate the photograph into a short semantic scene brief before designing.
For the shoulder-ride photo, "a playful child above an adult, riding on their
shoulders outdoors" is enough. An inventory of exact braids, shoe straps,
facial features, finger positions, jacket seams, and window divisions anchors
the drawing to the photograph and is not the default brief.

Recompose from that brief: invent silhouettes, change proportions and head
angles, displace features, redesign garments, and simplify or replace setting
details. Preserve the general relationship and broad positioning, not
photographic accuracy. A shoulder ride should remain a shoulder ride, but
neither person needs the photographed face, limb arrangement, or camera angle.
Choose the central carrier and shared shapes first, not after reconstructing
the photographed bodies. Do not impose portrait likeness or exact expression
unless the user explicitly requires it.

By default, inspect the photo, extract the brief, then supply only the selected
artwork references to the image tool. The brief carries the photo's subject
information without giving the model a photographic composition to preserve.
If a genuinely necessary user-required detail calls for including the photo,
label it as a loose content guide subordinate to the artwork references, and
identify that specific requirement. Do not use "edit only," "keep everything
unchanged," or "preserve all identifying details" for this reinterpretation.

Judge topic fidelity and style fidelity separately. First ask whether the
activity, subjects, and broad relationship read. Then ask whether the drawing
was actually invented in the skill's non-anatomical language. Recognizable
photo contours with flat fills and scratches still fail the second question.
Exactness explicitly requested by the user is a scoped exception, not a new
default requirement to reproduce the rest of the photograph.

## Style in one sentence

Non-anatomical figurative inventions built from irregular flat color silhouettes,
displaced single-eye features, impossible head-neck connections, and broken black
marks, with emotional meaning carried by gesture and overlap rather than
believable body mechanics.

## Color structure

Compare the [full family palette](../assets/source-family.png) and
[full drummer palette](../assets/source-drummer.png) as separate arrangements.

These are approximate visual working swatches, not measured paint matches.
Favor relationships over exact hex values; lighting and reproduction affect
the original images.

| Role | Approximate starting color | Behavior |
| --- | --- | --- |
| Turquoise | `#51ADB2` | Muted blue-green face or figure mass; not luminous cyan. |
| Oxide rust | `#B85D43` | Earthy red-orange face or figure mass; not pink flesh shading. |
| Mustard ochre | `#CEA33F` | Hair or selected face/clothing; warm rather than metallic. |
| Near-black | `#171714` | Contours, pupils, hair clusters, selective hatching. |
| Off-white | `#F2EDDF` | Open ground and eye whites; avoid dazzling digital white. |
| Optional cobalt | `#405B9A` | A secondary musician/clothing accent, not required in portraits. |

### Color choice and placement rules

These are working rules derived from the visible relationships in the two
separate paintings, not measured color ratios or claims about the artist's
intent. Explicit user palette requests can override the default hues without
requiring a change to the flat construction.

1. **Choose one coherent palette.** Start with three chromatic families plus
   near-black and off-white. For the family treatment, use muted brick/oxide
   rust, dusty turquoise, and ochre. For the drummer treatment, use earthy rust,
   ochre, and muted cobalt. Do not automatically combine turquoise and cobalt
   or introduce additional colors for every object. In a photo transformation,
   rebuild the palette rather than reproducing every garment, cushion, and
   lighting color; preserve particular source colors when explicitly requested.
2. **Keep the hues muted but distinct.** Rust should read as an earthy red,
   turquoise as a dusty blue-green, and ochre as a dull golden yellow. Avoid
   candy red, electric cyan, lemon yellow, and lifelike pink flesh. Do not mute
   everything into the same brown or apply a universal sepia wash. The hex
   swatches above are starting points, not exact matches or mandatory values.
3. **Give color an unequal spatial hierarchy.** Assign the largest fields to
   figures and major connecting shapes, then reserve smaller areas for echoes
   and accents. An ochre hair ribbon can connect distant parts of a group;
   a blue garment can counter a large ochre instrument. Do not give every hue
   equal area or add arbitrary percentage quotas unsupported by the reference.
4. **Use continuity to clarify interlocking people.** Usually carry one main
   exposed-body color through a person's face, neck, arms, and hands, including
   separated visible fragments. A turquoise person beside a rust person can
   remain readable despite impossible anatomy. Clothing may differ. Repeated
   figure colors are allowed when contours and placement distinguish people;
   do not alternate mechanically or equate color with gender or personality.
   Split a face only for an intentional plane or shared-profile construction,
   not as a routine two-tone portrait effect.
5. **Repeat colors instead of multiplying them.** Echo an existing figure color
   in small clothing marks, jewelry, or another relevant detail. In the family
   reference, turquoise details recur within rust fields. Use such repetition
   selectively, not as compulsory dots or copied accessories. An eye can use
   off-white and near-black directly against the main face field; the repeated
   turquoise eye patches in rejected tests are not a style requirement.
6. **Let white participate in the composition.** Preserve light neutral ground,
   gaps, and selected unfilled garments or objects as substantial shapes.
   Off-white is not just an eye-white or a border around filled figures.
   Do not automatically replace the open ground with a dark room or yellowed
   parchment because the photograph is dark. A requested scene background can
   differ, but should support rather than bury the figure-color relationships.
7. **Use black to articulate, not model.** Concentrate near-black in pupils,
   selective contours, hatching, and occasional hair or other relevant masses.
   Vary its density; do not give every color field a uniformly heavy enclosure.
   Preserve the underlying hue through sparse scratches rather than covering
   every surface with black noise or realistic shadow.
8. **Make color boundaries describe shapes, not lighting.** Keep fills broad,
   matte, and nearly uniform in value. Allow small coverage gaps and uneven
   edges, but no gradients, glossy highlights, blush, rim lights, or blended
   skin shadows. Separate touching forms through hue, a selective contour, or
   open ground rather than sculpting their volume.

Before prompting, state the chosen palette and its roles in one short sentence.
For example: "Rust and turquoise distinguish the two figures; ochre hair links
them, a few turquoise details repeat in the rust clothing, and off-white ground
and garments keep the arrangement open." This describes a color plan, not a
mandatory arrangement or proof that the drawing matches the style.

## Shape and anatomy

### Cranium, cheek, jaw, and chin

Use an irregular oval, taper, or blunt angular silhouette rather than a perfect
ellipse. Let the forehead, nose, lips, and chin change direction abruptly along
the outer edge in profile. In near-frontal views, the nose may instead be a long
interior line. Vary broad/short and narrow/long heads; do not clone one template.

Keep the cheek fuller and let it taper into a softly rounded asymmetric chin.
An elongated head need not have a sharp tip: the user rejected a needle-like
point. Locate the taper in the head's own orientation, sideways for a sideways
head, not automatically downward on the page. Preserve small contour changes
instead of reducing every head to an egg or a triangular wedge.

Flatten the cheek into the main face field. A short scratch or spare jaw contour
is enough. Avoid sculpted cheekbones, modeled temples, complex facial planes,
and photographic foreshortening. Preserve human recognition without conventional
portrait completeness.

Do not make "long angular nose" mean a generic animal snout. However, horizontal
heads, displaced jaws, and impossible connections are not errors by themselves.
Judge the particular arrangement against the reference. Do not restore a
believable skull, jaw, or forehead-to-chin sequence to make it more human.

### Eye and brow

Start with one clear eye; a second eye is optional, not a feature to carry
forward automatically from earlier two-eye tests. Honor an explicitly required
count. Eye alignment belongs to the head, not the upright neck or page.
With a full 90-degree roll, the pair is page-vertical and each eye's complete
eyelid/corner construction is also quarter-turned. Do not just stack upright
eye drawings or preserve body-aligned lid bars inside rotated eye patches.
Keep one pupil per eye and enough irregularity to avoid a repeated symbol.

Inspect the eye opening separately from its color patch. A long vertical
turquoise shape with a horizontally drawn eye inside it does not satisfy the
sideways orientation. Establish the eyelid arcs and corners in the rolled
head's frame, then place the patch around that eye without turning it upright.
If the optional second eye reintroduces a conflicting axis, omit it rather
than treating its presence as more important than correct orientation.

Two eyes do not mean two identical white diamonds with centered dots. Give
them unequal openings, slightly different size and spacing, offset pupils,
and different contour emphasis. One may be more compressed or partially
described, but both must remain visible when two are requested. Preserve
orientation without rigidly mirroring or mechanically repeating the drawing.
Keep the eyes relatively small within broad face fields, not dominant symbols.

For the approved individual-head treatment, use one visible eye per person.
Place it off-center in a broad uninterrupted face field. Its outer shape can be
an uneven almond, narrow wedge, or small irregular opening. Use off-white with a
dark pupil; a little face-color iris is optional. Vary pupil placement for gaze.

Use a single spare brow stroke where useful. Avoid neat matching eyelids,
realistic lashes, glossy catchlights, or adding a second eye to resolve the
perspective. Do not turn the omitted eye into a closed-eye symbol or empty socket.

The eye can be more frontal than the profile-like nose. This deliberate mixed
viewpoint is part of the simplification, not an error to anatomically repair.

### Nose

Use a long straight or slightly bent descent followed by a short step or hook.
In profile, integrate it into the silhouette. In near-frontal views, let one
interior line describe the bridge and base without describing both sides.
A tiny nostril mark may suffice. Skip shaded nostrils and a rounded modeled tip.
Do not require a closed triangle on every face. An open corner, incomplete
hook, or uneven bent stroke can do the work. For the refined sideways treatment,
omit the long line connecting the hair-side edge to the nose.

### Mouth

Use one short dash, a tiny angular notch, or two compact irregular marks.
Keep it small relative to the face and usually restrained. Do not default to
smiling, full outlined lips, glossy lips, or a long dark muzzle seam.
Let some mouth contours be faint, broken, or incomplete. A sideways mouth can
have an upright-on-page orientation without becoming an identical dark barcode
on every face. Give its weight and scale a different role from the nose.

### Ears

Use one loose curl, C-shaped mark, or irregular loop. Its placement is a
compositional decision, not a landmark constrained by the eye line, nose base,
jaw hinge, or physically correct head turn. It can sit inside a color field or
at an unexpected contour junction when that follows the source's construction.

Do not keep a realistic ear-jaw-neck alignment as a hidden anchor while merely
distorting the outline and nose. That still reads as an anatomical portrait.
Compare the ear's relationship to the eye patch, facial marks, head edge, and
neck separately. Omit the ear if it contributes nothing; do not mechanically
relocate every ear to the same unusual point or add detailed cartilage.

### Neck and shoulder

Let an elongated, uneven neck flow into the jaw. It can narrow, bow, or form
an S-curve; avoid a perfectly cylindrical stem with realistic muscle rendering.

Compose strong bends through unequal contour lengths, abrupt joins, and
unexpected attachment points. A neck need not connect correctly beneath a jaw;
an ear need not occupy its expected anatomical position. Keep shoulders spare.
The relationship should be expressive and source-led, not a demonstration of
how an actual neck flexes.
In the accepted sideways treatment, keep the full lower head curve readable,
partly as an interior line at the neck overlap. Let only a short segment flow
into the neck. A continuous color field does not require erasing the boundary
that makes the head recognizable; conversely, do not outline a detached head
all the way around and perch it on a straight rectangular stalk.

### Hair

Use two main vocabularies: ochre masses with a few long searching ribbons, or
near-black clusters of scratchy directional strokes. Curls are irregular loops,
not repeated identical coils. Allow gaps and overlapping strokes.

For female characters, default to long hair in this style unless the user
explicitly requests another treatment. This is an art-direction choice for the
skill, not a claim that hair length determines gender.

Separate attachment from fall:

- Anchor the hairline, roots, crown, and part to the head's sideways orientation,
  never to an imagined upright scalp or to the neck.
- Let the free lengths then bend and hang downward with gravity. They may pass
  beside or across the neck, but their origin remains visibly on the tilted head.
- Use the change of direction from rotated roots to falling lengths to reveal
  the head bend. Keep enough of the cheek and lower head contour exposed.

For the sideways-head treatment, do not place a cap or bridge of hair across
the side of the head facing the top of the image. Leave that head contour
exposed against the ground. Start the hanging mass at the back-side attachment
and flow downward; do not loop it over the upper edge to join opposite locks
or to complete a conventional anatomical scalp. Mirror the attachment for a
mirrored head, but keep the free lengths falling toward the image bottom.

Do not rotate the entire long hairstyle into a rigid sideways flag. Conversely,
a conventional upright hairstyle draped beside a sideways face is not enough.
The roots and the free lengths have different directional responsibilities.
This refines the earlier whole-haircut rotation rule: head-led attachment and
gravity-led lengths work together, without anatomically correcting the face.

Hair can guide the eye around a face and through a group without realistic
strand simulation or glossy highlights. Expose enough of the head contour and
neck junction to keep their relationship readable.

### Bodies, arms, and hands in complete scenes

Extend the same reduction rather than attaching polished anatomy to a rough
head. Use broad garment and limb shapes, bending contours, and overlaps.
Hands may be expressive and enlarged when the action calls for them; do not
make giant hands a compulsory motif. Clarify contact through placement rather
than rendering every joint. Do not invent ownership of ambiguous overlapping
limbs when analyzing a reference.

## Movement and emotional construction

Distinguish three independent changes:

- Roll: tip the head toward a shoulder.
- Pitch: lift the chin or bow it toward the chest.
- Turn: face left, right, or partly toward/away from the viewer.

Use these directions to describe visual variation, not as rules of body
mechanics. The eye, nose, mouth, and head outline need not share one coordinate
system. Allow independent rotations, shifts, and scale changes where the
reference suggests them. A sideways-looking face can join a rising neck in a
physically impossible way. Do not replace this with an ordinary portrait
rotated as a rigid unit.

Use long neck contours, abrupt bends, opposing head angles, and shoulder
diagonals to establish rhythm. Emotional gesture takes precedence over
anatomical plausibility, without requiring grotesque detail or animal features.

In a musician, a deep bend and downward/sideward attention can suggest absorption.
In a group, opposing bends and interlocking contours can suggest intimacy.
Treat these as design readings, not universal psychological meanings.

### Sideways-head construction

Inspect [the accepted pose study](../assets/accepted-sideways-head.png).
Compare the [original family](../assets/source-family.png) for its richer
irregular relationships, not the rejected swan-neck attempts.

- Establish a full 90-degree facial roll across a rising neck. The implied
  ear-to-ear axis is vertical and forehead-to-chin axis horizontal; this is a
  spatial aid, not a realistic skeleton or a request for two visible ears.
- Position the cheek over the neck rather than translating a detached head
  around on a stem. Retain the full head's lower cheek-jaw curve.
- Blend only a short local junction into the neck. Do not broaden the neck
  until the sideways head disappears into a long slope.
- Keep the requested eye count and orient the whole eye marks with the head.
  Their size, shape, spacing, and stroke emphasis need not match.
- Preserve non-anatomical placement without converting features into a fixed
  set of geometric symbols. Omit the long hair-to-nose line.
- Keep the fuller cheek, soft asymmetric chin taper, downward hair, and exposed
  image-top-facing head edge established by the user's refinements.

The accepted pose is a construction reference, not a template to clone
unchanged. For different people, vary forehead and cheek breadth, chin offset,
eye opening, facial spacing, and mark emphasis as well as hair and color.
Judge each result against the references; new studies remain provisional.

## Depth, hair, and shared shapes

### Central carrier and visual handoffs

Inspect the [hair-handoff close-up](../assets/family-handoff.png) beside the
[complete family composition](../assets/source-family.png).

Use a central organizing element as the movement engine of a complete
composition. "Central" describes its connecting role, not a required position
at the canvas center. This is a working principle for this skill, not a claim
that every work by an unidentified artist follows one universal formula.
Choose a subject-bearing carrier such as hair, linked gestures, an instrument
arc, or a shared facial boundary; let other movements feed into it.

The user's mother-to-daughter reading of the family hair identifies a visual
handoff. The ochre flow around the upper rust profile descends into a narrowing
junction beside the smaller sideways rust head. The neighboring hair contours
pick up and extend that descent into the long lower sweep. Attention can follow
one continuous movement even as its apparent association passes from one
person to another. Do not break this into independently completed hairstyles
merely to make anatomical ownership unambiguous. Equally, do not interpret it
as an instruction to grow hair literally from another person's neck.

A useful handoff has an approaching direction, a receiving form, and a
specific junction: curves converge, overlap, share an edge, or continue
across a small interruption. The receiving form can change the direction or
width while preserving enough continuity to carry attention onward. Similar
colors in disconnected locations can reinforce a handoff, but are not the
handoff themselves. Nor does it require people to hold hands.

Faces use the same principle through shared shape rather than only a traveling
line. One profile supplies an edge that the other profile also needs. The eye
can switch between each individual and the combined shape, including the
hidden heart identified by the user. This is a perceptual handoff: a boundary
changes which person it describes, and the people together produce a further
reading. Two complete faces placed inside a heart outline do not achieve it.

Before detailing a new group, state the carrier, the passing junctions, the
receiving forms, and the larger shape or return route they create. For example:
"The upper figure's descending hair narrows beside the smaller face, whose
hair picks up the curve and carries it toward the foreground arm; that arm
turns attention back into the group." Preserve distinct people without sealing
every person inside a separate outline. Judge whether the handoffs remain
legible when small details are ignored; do not add ribbons or connectors
unrelated to the subject simply to close a loop.

### Drummer: compressed depth without modeled volume

Compare the [hands-and-instruments crop](../assets/drummer-depth.png) with the
[complete drummer](../assets/source-drummer.png) to retain the near/far context.

The drums and hands project toward the viewer while the shirt and small bent
head sit farther into the composition. The large ochre drum at the lower right
dominates the foreground and continues beyond the lower and right edges.
The other drum enters from the left. Their broad white heads and curved rims
provide tilted surface planes against the upright lengths of the shells.
These directional changes supply depth even though the fills remain flat.

The enlarged hands overlap the drumhead and rim regions; visible fingers place
the action at those surfaces. The instrument masses obscure much of the lower
body, leaving the blue clothing as an irregular connecting shape between them.
Above that, the white shirt recedes between the reaching arms and beneath the
smaller rust head. The brim crosses the head, adding another local overlap.
Size exaggeration makes the playing hands important as well as near; it is not
a consistent anatomical perspective calculation.

One plausible attention circuit is the bent head and brim, down an arm to one
hand, across the contrasting white drumhead arcs to the other hand, then back
through the shirt's marks and surrounding musical curves. The opposed drum
angles and finger directions interrupt that circuit rhythmically rather than
forming a static symmetrical pair.

For a new musician, preserve the contact and near/far hierarchy rather than
copying these instruments. Let foreground action overlap the torso and let
background signs sit behind the silhouette. Use selective contour interruptions
to show which shape covers which. Do not repair the deliberately inconsistent
perspective or add gradients to make the instruments volumetric.

### Family: hair as a moving connection

Trace the [hair close-up](../assets/family-handoff.png) within the
[full family](../assets/source-family.png), rather than treating it as an
independent hairstyle reference.

The ochre hair is a broad continuous route through the family, not a hairstyle
drawn separately around every face. It curves around the upper rust profile,
narrows between the upper grouping and smaller heads, and sweeps down through
the lower composition. The mother-to-daughter handoff described above lets
that movement change apparent ownership without starting over. Its changing
width creates both a color mass and a
directional ribbon. Several uneven internal strokes repeat its bends rather
than describing individually shaded strands.

The hair's long descent is countered by the smaller rust head extending
sideways and by arms crossing diagonally below. These changes of direction
pass attention between faces and gestures. Where hair lies beside or overlaps
a face, shoulder, or arm, the boundary helps define both shapes; it also opens
and closes small gaps of ground. Darker local tangles slow attention at a
junction, while a broad quiet ochre stretch carries it onward.

In a new composition, give the hair a specific attachment, route, overlap, and
destination. Keep roots aligned to their head and loose lengths falling
downward as established for the sideways treatment, but let the descending
curve participate in the whole arrangement. Do not replace it with a stiff
straight curtain, arbitrary windblown strands, or an unattached decorative
ribbon. Retain the exposed upper-head contour in the refined sideways pose;
the original's hair placement does not override that later correction.

### Family: several people construct one larger shape

Inspect the [merged-profile crop](../assets/family-merged-profiles.png) and
[full group](../assets/source-family.png) at both individual and combined scales.

Read the family at two scales: distinct people and a single interlocked
arrangement. The user's reading of the upper rust and turquoise profiles as a
hidden heart is one example: a larger shape emerges from people sharing a
boundary, not from an emblem added behind them. That heart interpretation
does not explain every overlap or prescribe a heart for a new subject.

The smaller turquoise and rust heads below point in different directions.
Their necks and shoulder slopes meet the descending hair and neighboring
bodies, making linked bends rather than a row of separate busts. The long
lower arms introduce a crossing diagonal beneath these heads. Together,
head contours, neck strips, hair, and arms create larger sweeping curves,
tapered enclosures, and wedge- or crescent-like gaps. Both the colored forms
and the spaces they leave matter. A contour can belong to one person's
silhouette while also shaping the adjacent person's visible space.

One plausible visual loop starts at the large upper eyes, moves toward the
raised hand at the upper right, drops to the smaller rust face, follows the
ochre descent to the lower arms and hand, then returns through the smaller
turquoise face and the leftward hair curve. Repeated turquoise and rust
accents offer shorter connections across that route. This describes available
visual cues, not a measured eye-tracking result or a fixed viewing order.

For a new group, first choose the larger shared curve or enclosure. Assign
segments to different people's head, back, hair, or arm, then establish
overlaps and negative spaces. Keep intentional contact and enough identifying
marks to read each person. Do not force bodies into a literal geometric logo,
invent limb ownership in ambiguous source passages, or fully finish isolated
figures and merely place them next to each other.

### Moving groups: transfer the street-dance lessons

Use the dance study to extract compositional mechanisms, not to promote the
latest generated image to an approved style reference.

- **Stage depth in three readable layers.** A nearer hand, shoe, or garment edge
  can be enlarged and overlap ground markings; overlapping figures occupy the
  middle; smaller vehicles and interrupted building contours sit behind them.
  Keep contact with the ground readable. Scale can emphasize action without
  enforcing realistic anatomy, and recession needs neither shading nor blur.
- **Create movement through counter-directions.** Contrast a lifted knee with
  an extended arm, a sideways head with a rising torso, and one dancer's lean
  with another's turn. Alternate compressed and stretched shapes rather than
  repeating three matching poses. Suggest a passing moment through a raised
  foot or turning hem; motion lines cannot rescue static construction.
- **Share gestures and the spaces they enclose.** Two raised arms can form one
  arch belonging to two people, while bent legs and adjacent bodies make
  smaller wedges and crescents below. Keep the meeting hands legible and
  distinguish touching from accidental tangency. Not every group must hold
  hands: choose contact or near-contact that fits its actual activity.
- **Continue the gesture through hair and clothing.** Broad descending hair
  curves can bridge the upper arm movement and lower skirt or leg movement.
  A turning hem can redirect attention toward the next figure. Keep hair
  rooted in its own head with loose lengths falling downward; different
  bodies need not have identical hair sweeps or an invented common wind.
- **Make the setting participate without taking over.** In the NYC study,
  crosswalk diagonals establish a ground plane and echo the steps; upright
  facades and fire-escape zigzags counter the figures' curves. Smaller rear
  city details establish place. For another setting, choose equivalent
  subject-related structures, not compulsory crosswalks or taxis. Interrupt
  environmental lines at foreground figures and reduce their density near
  faces, hands, and shared gaps; do not fill all open ground with architecture.
- **Connect near and far movement into a loop.** A plausible route is a
  foreground step, a rising body, the joined hands, an adjacent face, a
  descending hair mass, and another dancer's step. Repeated colors can connect
  across it. Describe the forms carrying attention rather than adding arrows;
  this remains an interpretation, not a guaranteed viewing sequence.

## Fused profiles and hidden symbolism

This is an optional compositional technique, not the default for every head.
The user read the large upper family form as a man and woman in opposing
profiles who morph together and form a heart.

Give each person one eye, but let forehead/nose/mouth contours do double duty.
The union should permit two readings: two people, and one apparent frontal
head. Color masses touch rather than leaving a white gap. Shared marks can
remain ambiguous instead of supplying two complete noses and two complete mouths.

Suggest a heart through the broad combined head contour, not an explicit frame
or necks meeting in a sharp decorative V. A hidden relationship should emerge
after the people register. Do not force this symbol into unrelated scenes.

## Surrounding details and subject meaning

Treat the surroundings as part of the subject's story, not filler added after
the figures. The user identifies these details as meaningful. Preserve that
principle without claiming to know the artist's intended meaning of each mark.
Separate what is visible from a possible reading.

### Details visible in the supplied originals

These observations refer to the [family](../assets/source-family.png) and
[drummer](../assets/source-drummer.png), not the generated head sheet.
Reinspect those bundled sources when exact shapes or placements matter.

| Detail and placement | Relationship to the subject |
| --- | --- |
| Drummer: large treble-clef-like musical sign at the upper right, with loose directional strokes around the player. | Music is present beyond the physical drums. The curves and changing stroke directions can extend the hands' rhythm into the surrounding space; they are not generic distress. |
| Drummer: the paired drumheads, rims, and large ochre shells fill the foreground around the hands. | These are the surfaces being played. Keep hand-to-drum contact and overlapping rims readable; their arcs and diagonals carry the action. |
| Drummer: ochre brimmed hat, dark hatband marks, and sparse shirt details. | These distinguish the depicted performer and repeat existing shapes and colors. Their specific cultural meaning is unverified; they are not mandatory accessories for every musician. |
| Family: a slender stem with leaves and a white flower-like bloom at the upper left, rising from an outlined container. | This is a recognizable setting detail beside the group, not a random flourish. It can contribute a sense of a tended environment and echo the figures' rising curves; that reading is not confirmed symbolism. |
| Family: horizontal bands and loosely rectangular setting lines behind and between the figures, plus short curved strokes at the right. | These give the interlocking people a shared surrounding space while leaving the ground open. Preserve their placement and varied direction without asserting an exact building, landscape, or meaning for ambiguous strokes. |
| Family: turquoise spots on rust clothing, a small sequence of turquoise necklace-like marks, and an outlined white chest motif on the lower turquoise figure. | Personal details distinguish the figures and repeat the palette across them. Retain the chest motif's visible shape when studying this source without confidently naming an ambiguous design. |
| Family: long ochre hair threading through the group, overlapping arms, and the large hand beside the upper figures. | These are subject-bearing connections, not background texture. Their routes, contact, and overlaps help the figures read together. Do not invent ownership where the source is ambiguous. |

Visible heading text in the supplied reproduction supplies family/music context,
but do not assume all overlaid text or reproduction marks belong to the original
painting. Do not copy watermarks, branding, or unrelated titles into new work.
See the typography section below for the visible letterform treatments.
The user's hidden-heart reading belongs to the shared-profile construction,
not an instruction to scatter heart icons around a family.

### Apply the principle to a new subject

For each retained detail, establish its identity, subject-related role, and
position relative to the main action. Use a short prompt sentence describing
that relationship rather than a disconnected list of props. Simplify detail
through selective contours and flat shapes, not by deleting its meaning.

For a child cradling an infant, a supporting lap and a spare cushion shape
can explain the seated embrace. Clothing marks or sock stripes may contribute
rhythm, but the photographed ties, patterns, colors, and furniture are not
mandatory likeness cues. Select, redesign, or omit them according to their
role in the new composition. Preserve meaningful context rather than literal
objects; do not import a musical sign or flower just because one occurs in
the paintings.

Keep environmental contours lighter or more interrupted where they would
compete with faces and contact points. Let their curves or diagonals lead toward
or echo the action. Leave quiet gaps between them. Structural setting lines,
narrative objects, and incidental surface scuffs have different jobs; adding
more scuffs cannot replace missing context.

## Typography and image integration

Describe the lettering visible in the supplied reproductions separately from
the painted marks. Its exact font, method of production, and status as original
painting content versus an added title are unverified.

### Family reproduction

Inspect the [family heading crop](../assets/typography-family.png) in the
[full image](../assets/source-family.png) to see its overlap with the figures.

The visible "FAMILIA" heading uses very large black uppercase, serif-style
display letters. Heavy upright strokes contrast with finer bars and serif
details. The letters have a relatively regular typographic structure rather
than the loose searching contours of the figures.

The word stretches across the top and overlaps the ochre hair and upper colored
head shapes instead of occupying a separate white title banner. Parts approach
or meet the image edges, with outer lettering cropped in the supplied views.
Its strong horizontal span provides a counterweight to the long descending
hair. Solid black letter masses also offer a contrast to the broken black
drawing. These are visible compositional relationships, not proof of intent.

### Drummer reproduction

Inspect the [drummer heading crop](../assets/typography-drummer.png) in the
[full image](../assets/source-drummer.png) to compare the two text treatments.

The large upper heading has a loose brush- or calligraphic-looking character:
changing stroke weight, irregular curves, and a less mechanically even rhythm.
The smaller "BUENA" line beneath uses comparatively thin, regular uppercase
sans-serif-looking letters. Their contrast supplies a clear large/small
hierarchy; do not describe both lines as the same distressed display type.
The heading's irregular rhythm can be read alongside the musical gestures,
without claiming a specific font, cultural origin, or lettering technique.

### Rules for new lettering

Include lettering only when the user requests it or explicitly includes it in
the intended composition. Choose wording relevant to the new subject, not a
copied family or music title. Establish the exact wording before rendering
when it has not been supplied.

Choose the treatment deliberately: large structured display capitals can
anchor a composition, while loose expressive lettering can echo an action.
Keep secondary text smaller and quieter rather than making every line equally
expressive. Use the existing near-black or another selected palette color;
avoid automatic outlines, gradients, shadows, badges, and added hues.

Plan scale, spacing, and placement alongside the figures. Text may overlap
selected color fields, but should not erase a focal eye, meaningful hand
contact, or the central visual handoff. Do not force all letters to imitate
paint scratches: relatively crisp type against rough drawing is itself a
useful contrast. Cropping is an observed source treatment, not permission to
truncate required words. Check actual spelling and readability; disclose
rendering errors instead of treating approximate lettering as correct.

## Line and texture

Distinguish structural contours, internal feature marks, and surface scratches.
Contours carry recognition and generally have more weight; feature marks are
selective; scratches should not compete with either.

Vary pressure, continuity, and direction. Retrace locally with slightly offset
strokes; leave some edges unresolved. Concentrate hatching in selected hair,
overlap, and contour areas rather than encircling every shape in equal black.

Texture should look incidental to drawing and imperfect coverage. Preserve
large quiet fields. A uniform noise layer, cracked-paint filter, or artificially
aged parchment cannot supply the style on its own.

### Unequal marks, not a face-symbol kit

The comparison reference had a full uneven head, a relatively small eye,
substantial angular nose marks, a faint mouth, and varied contour pressure.
Failed galleries reduced these to matching white eyes, closed triangles,
vertical dashes, triangular heads, and straight necks. More grain will not fix
that loss of relationships.

Vary strength, size, continuity, and placement within each face. Let some
contours be broad and others almost disappear. Keep outline rhythm uneven,
not a consistent thick enclosure around tidy filled shapes. Retain the later
hair and nose-line corrections even if a useful comparison image predates them.

## Prompt starters

Replace bracketed content with the actual request. Supply the approved image
through the image tool's reference input, not just its filename in prose.

### Individual or gallery

> Create [subject/count/framing] using the attached approved sheet as the primary
> guide. Build full uneven flat head silhouettes, [requested eye count] small
> irregular eye marks per individual, open angular nose strokes and faint
> incomplete mouths. Give features unequal emphasis rather than repeating
> diamonds, triangles, and dashes. [Specify pose and head-neck relationship;
> use the accepted sideways pose image when appropriate.]
> Invent the head-neck connection and allow independently displaced facial marks;
> retain the spare mixed-viewpoint construction rather than rotating an ordinary
> anatomical portrait. Compose the ear mark independently too; do not anchor it
> in a conventional portrait position beside the jaw. Use muted turquoise, rust,
> ochre, off-white, and broken
> black marks. Keep broad unshaded color masses and selective scratches.
> [State the selected palette's large fields, connecting mass, small repeated
> accents, and open-ground role; do not automatically use every swatch.]
> Avoid realistic portrait anatomy, sculpted cheekbones, smooth shading, polished
> outlines, and animal-like muzzles. [Requested exclusions/framing.]

### Morphing pair

> Create an original paired portrait using the approved sheet for feature economy,
> flat color, and uneven drawing. Construct two opposing single-eye profiles whose
> touching color masses and shared nose/mouth contours also read as one apparent
> face. [Describe relationship and gesture.] If requested, let the combined head
> subtly suggest a heart. No separating gap, two complete kissing silhouettes,
> literal heart frame, or merely recolored conventional frontal face.
> [Describe how different people's contours form a larger curve or enclosure,
> the shared boundary that hands the reading between people, the gaps between
> them, and the larger shape that emerges without a separate outline.]
> [Describe subject-related setting or personal details and their placement;
> use them to support the relationship, not as an unrelated decorative border.]

### Absorbed musician

> Create [musician/action/framing] in the approved sheet's simplified visual
> language. Deeply bend the head sideways and downward relative to the shoulders;
> use impossible flat-shape connections and spare displaced features rather than
> believable neck mechanics. Let the uneven neck and shoulder relationship
> communicate absorption in playing. Preserve figurative ambiguity without a
> generic animal snout or an anatomically corrected portrait.
> [Include a hat only if requested.] Use spare black contours and broad flat
> earth-red/ochre fields with selective cool accents.
> Keep contact with the instrument legible. [Describe music-related surrounding
> marks or setting details whose placement extends the action into the scene.]
> [State foreground action, the overlapping torso and rear head placement, and
> how instrument edges and gestures circulate attention without modeled shading.]

### Moving group or street scene

> Create [subject/count/activity/setting] as one interlocking flat arrangement,
> using the approved references for construction and finish. Give each person
> a different lean or turn, contrasting compressed and extended gestures.
> [Name the central carrier, where one person's form hands movement to the next,
> and the shared curve or arch and open gaps their combined shapes create.]
> Establish [near action], [overlapping middle figures], and [smaller rear
> setting details] through scale and contour interruptions, without shading.
> Let head-rooted descending hair and responsive clothing carry attention
> between faces, hands, and steps. [Name the meaningful contact points and
> setting lines that reinforce the action.] Preserve the selected limited
> palette, quiet fields, and non-anatomical connections; do not substitute
> motion lines, realistic anatomy, or dense background detail for movement.

### Photo-inspired scene

> Create an original non-anatomical painting about [short scene brief: subjects,
> activity, broad relative positions, and general setting]. The photograph
> supplied this topic only; it is not the target drawing. Use the attached
> artwork references for invented silhouettes, facial construction, palette,
> and mark-making. Recompose freely rather than reconstructing photographic
> likeness, exact poses, clothing, camera perspective, or background layout.
> [Describe the central carrier, its handoffs, shared shapes, and depth layers.]
> Keep the basic relationship readable. [Only explicitly required exact details.]
> Do not make a faithful redraw with flat color and distressed texture.

## Diagnose drift before adding more texture

| Symptom | Correct the construction |
| --- | --- |
| Polished portrait with scratches | Remove anatomical modeling and excess feature detail; flatten the silhouette and color. |
| Photo-inspired image reproduces the photograph too accurately | Reduce the photo to a topic-and-relationship brief, omit it from image-tool inputs when that brief suffices, and recompose from the artwork references rather than preserving likeness or exact geometry. |
| Correct hues but an unrelated color composition | Reassign unequal large fields, connecting masses, repeated accents, and open ground; palette matching alone is insufficient. |
| Figures surrounded by meaningless scribbles or stripped of context | Restore subject-related objects, setting lines, and personal motifs in specific relationships to the action; simplify their drawing, not their meaning. |
| Flat color becomes a flat stack of disconnected objects | Establish near/far overlap, scale changes, cropped foreground forms, and contact surfaces without adding shaded volume. |
| People read as separate portraits placed together | Build a shared curve or enclosure from different people's contours; connect focal points through hair, gestures, repeated colors, and intentional gaps. |
| Movement stops at each person's silhouette | Choose a dominant carrier and build specific receiving junctions where hair, gestures, or shared contours pass movement onward; matching colors alone do not create a handoff. |
| Moving figures feel static or synchronized into one template | Contrast their leans, compressed and extended gestures, and lifted steps; carry those directions through hair and clothing without adding generic speed marks. |
| Detailed setting overwhelms the action | Keep rear forms smaller and selectively drawn; interrupt their contours at nearer figures and preserve open gaps around focal gestures. |
| Every face has a turquoise eye patch | Remove automatic patches; use the main face field, a spare off-white opening, and selective black marks unless a patch has a specific compositional role. |
| Animal or beak-like head | Compare the specific silhouette and feature placement with the source; do not fix it by restoring realistic anatomy. |
| Sideways head reads as a generic muzzle | Break the repeated snout template with source-specific asymmetry and displaced marks; horizontal orientation itself is not forbidden. |
| Believable portrait merely tilted | Invent the attachment and redistribute features; do not enforce a shared facial coordinate system. |
| Realistic ear placement anchors an otherwise distorted head | Recompose the ear's relationship to the other marks and neck from the source; do not preserve anatomical ear-jaw alignment. |
| Requested two-eye study becomes matching icons | Keep the requested count and head alignment, but vary eye opening, pupil offset, size, and contour emphasis. |
| One-eye treatment becomes a conventional two-eye face | Return to the requested single-eye omission and selective mixed viewpoints. |
| Whole head disappears into the neck | Restore the lower cheek-jaw curve and blend only a short junction. |
| Head perches on a rectangular stalk | Preserve the complete head while varying and locally blending its overlap with the neck. |
| Repeated diamond-triangle-dash faces | Use unequal scale, spacing, pressure, and incomplete marks; change facial construction, not only hair and color. |
| Identical poses with new colors | Change roll, pitch, turn, silhouette, and neck curvature deliberately. |
| Tilted hair over an otherwise conventional portrait | Recompose the head, features, and neck as an intentionally non-anatomical relationship, not just a hairstyle change. |
| Sideways face with an upright hairstyle or neck-rooted hair | Attach roots and part to the sideways head, then let long loose lengths fall with gravity. |
| Long hair projects rigidly sideways | Keep the rotated attachment, but bend the free lengths downward to reinforce the head's orientation. |
| Hair arches over the image-top side of a sideways head | Remove the cap or bridge, expose that head contour, and keep the hair flowing downward from its back-side attachment. |
| Two people shaped like a heart logo | Remove the gap/frame and share facial contours instead. |
| Dense grain everywhere | Restore quiet fills and concentrate marks where they explain form or gesture. |
| Attractive but no longer like the reference | Reinspect the approved sheet; do not promote the newest output to authority. |
