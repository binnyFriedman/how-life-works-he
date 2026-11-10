# 5 Networks

                         Networks
                   The Webs That Make Us

As the Human Genome Project motored on in the 1990s, some researchers
were already warning that we would not stand much chance of interpreting
its findings until we understood more about how all these genes and the
proteins they encode work together. The existence of transcriptional
regulation had recommended the notion of thinking about so-called gene
action not in linear terms—this gene makes this protein, which catalyzes
this reaction—but as a network. The idea was that genes were speaking to
one another, and the task was to figure out who was conversing with whom:
to map out not just the genome but the connectome through which it
operates.
   The implicit picture behind all this was one in which molecules held
selective conversations. The cell was awash with jigsaw pieces that fitted
together only in very particular ways, creating an interaction network that is
precisely defined. Information passed through the cell along well-defined
channels which we can plot much as we might for a computer’s logic
circuits. Cell biologist Dennis Bray wrote in 2009 that “protein complexes
associated with DNA act like microchips to switch genes on and off in
different cells—executing ‘programs’ of development.”
   In the early 2000s this enterprise of mapping out the cell’s circuitry
became a key facet of the discipline christened systems biology, which had
the laudable aim of moving beyond a reductionistic characterization of all
of nature’s molecular parts to a view—and ideally a predictive model—of
how they work together. The hope was that once the network was known it
would be possible to model it on the computer, so as to predict, for
example, the effect of inactivating this gene or that protein, perhaps by
pharmaceutical intervention. These networks maps were quite dizzying in
their complexity (fig. 5.1), and it was hard to make out the logical
principles behind them, if these existed at all. Nonetheless, perhaps a
comprehensive enough computer model could do the job by brute force, so
that we didn’t need to understand how the thing worked?
   This picture of gene circuits was fairly tractable and worked quite well
for simple organisms such as bacteria. Researchers could even rewire those
circuits, adding new components by genetic engineering that produced
predictable, designed effects on the organism. That enterprise, which
became known as synthetic biology, is discussed in chapter 11. And even
for more complex organisms, the power of the systems perspective could be
impressive. In 2012, developmental biologist Eric Davidson and his
colleagues showed that, using experimental data for the gene regulatory
network of the sea urchin, they could make rather accurate predictions
about which genes would be switched on or off in the network of fifty or so
key genes in the four main tissue types (called the endoderm, mesoderm
ectoderm, and skeletal micromere) of the embryo as it developed hour by
hour. It seemed that, knowing the “wiring diagram” of the network, one
could predict how gene activity would unfold. Impressive, yes—but it was
not (as some suggested) a comprehensive picture of how development
happened, primarily for the reason that it didn’t predict development at all!
All of the spatial information about where cells were and what shape the
developing organism took had to be put in by hand.
   That’s one of the problems with a systems approach like this: you can’t
simply read out shape and form from a knowledge of which genes are
active. And to truly understand what is happening even at the molecular
level, a “wiring diagram” of the gene regulatory network is not enough. As
we’ve seen, a lot of the regulation is conducted not by proteins but by
noncoding RNA molecules of many kinds. That was not obviously a
problem for the general principle: it just meant that the network had more
types of component, and more connections.
![Fig. 5.1 The network of interactions between some genes associated with breast cancer. Image](media/fig-5.1.png)

Fig. 5.1 The network of interactions between some genes associated with breast cancer. Image
courtesy of Emmert-Streib et al. (2014).

   There were, however, further difficulties with this picture. One puzzle is
that a gene’s regulatory elements seemed to be scattered rather haphazardly
through the genome. You would expect that, if DNA is a linear information
string, it would keep all the information relevant to a particular instruction
gathered in one place, rather than requiring the readout to involve scouring
the chromosomes for other bits of vital information. In particular, while
promoter elements tend to appear next to their genes, enhancer elements
could be many thousands of base pairs away. How does that work? And
why did nature seem to be so perverse?
   Another problem was that, for complex organisms like us, the network of
interacting molecules—the interactome—sometimes seemed not just
absurdly but impossibly complicated. The prevailing idea was that
biomolecules speak to one another in intimate, highly selective embraces.
Sometimes these exchanges demand the convening of several molecules at
once. For example, a regulatory RNA molecule might bind to a section of
DNA via base pairing in a sequence-specific manner, and then the RNA
could latch onto an enzyme that effects some chemical transformation, so
that the corresponding change happens at a sequence-selected location. That
is, for example, how the enzyme methyltransferase, with a very general
capacity to stick a methyl group onto a cytosine base of DNA, can conduct
selective epigenetic marking.
   But some of these interactions turn out to involve not just a few but many
molecules at once. Now, that’s not inherently implausible—we saw earlier
that the ribosome, the machinery for translating mRNA into proteins, is a
conglomerate of several components, including ribosomal RNA and
proteins. But it’s one thing to see such well-orchestrated molecular
cooperation for an operation so central to cell function that is happening
more or less all the time: it’s worth the cell, so to speak, taking the time to
build and maintain such a complex assembly.1 It’s more surprising to find
that the networks describing, say, how proteins pass messages around in the
cell have hubs that unite perhaps half a dozen of them at once, just for the
instant that the message is transmitted. That problem became simply
embarrassing when it came to understanding gene regulation. The
components that seemed to be required just kept multiplying, forcing
researchers to postulate transient “complexes” made from a dozen or more
molecules.
   One of these, from a 2003 paper on gene regulation, is shown in fig. 5.2.
What you’re really looking at here is a diagram not of a molecular event but
of a failed paradigm. Imagine it: amid the random noise of the cell, where
proteins are bouncing this way and that in a chaotically crowded
environment, their concentrations are constantly fluctuating, and when
unions between proteins are in any case temporary, being made and broken
all the time, you have to wait until all the right components just happen to
come together at the right time and place to form this incredibly
complicated and intricate structure. It’s not unlike hoping that a billiards
shot will send all the balls colliding in just the right way for them to reform
the triangular array in which they were sequestered before the opening
break shot. And what happens if one element is still missing? Will the rest
still kind of work, but not so well, or will it fail just like a watch mechanism
that lacks a cog?

![Fig. 5.2 This protein “complex” (each blob representing a different molecule) was postulated in the](media/fig-5.2.png)

Fig. 5.2 This protein “complex” (each blob representing a different molecule) was postulated in the
early 2000s to account for how some human genes are regulated. In reality, a well-defined entity like
this has a vanishing probability of forming and remaining stable in a real cell.

   As if this isn’t already bad enough, there’s another issue with the simple
network picture of systems biology. As we saw in the previous chapter, the
interactions between biomolecules in the cell aren’t always beautifully
selective, ensuring precise, reliable, and predictable channels down which
signals and information pass. In particular, some proteins lack the well-
defined shapes necessary for such exquisite molecular recognition to
happen—they might bind to a variety of other molecules, with varying
degrees of precision and stickiness. What’s more, that kind of promiscuity
is particularly common among the molecules at the heart of the interactome:
the proteins called transcription factors. Some of these bind to DNA
sequences or to one another without strong preferences for the exact
sequence. How do you define and model such a fuzzy network? And more
to the point, how can life reliably function amid such apparently casual and
ill-defined molecular transactions?
    If the first challenge to the conventional story of our own biology comes
with the recognition that genes don’t relate to traits in any straightforward
way, and the second comes from the discovery that our organismal
complexity lies not with the genes themselves but with how they are
regulated, the third major shift in thinking is that this regulation is not
governed by simple switching processes in a precisely delineated
interactome network. The reality is startlingly different, and there is plenty
about it that we still don’t understand. What we do know, though, is
astonishingly, gratifyingly ingenious. It reiterates the point that life has
rules at many different levels of organization that don’t relate in any
obvious way to those of the levels above and below. None is more
fundamental than any other.

In the Loop
Let’s take a closer look at how gene regulation occurs. In contrast to the old
idea of the genome as an orderly linear sequence of instructions, DNA
packaged into chromatin looks more like a cupboard stuffed full of
documents in a random heap of loose pages. Yet somehow there is precise
cross-referencing and coordination amid the chaos. In particular, expression
of a given gene can be influenced by an enhancer sequence that sits very far
from the gene itself. How can DNA act on itself over such a distance?
   The only plausible mechanism must involve some physical interaction
that involves bringing the two regions—gene and enhancer—together in
space by folding and bending the chromatin itself. In other words, the three-
dimensional shape of this tangled mass of DNA and protein is relevant to
the process. It’s hard to overstate what a perplexing idea this is. Chromatin
in its unraveled state (euchromatin) looks like a random mess (fig. 5.3).
How does any part of it find any other reliably and predictably? As
chemical engineer Andrew Spakowitz (whose work produced this image)
has put it, “Despite the fact that I have worked on chromosomal
organization and dynamics for the past twenty years, I am still baffled by
the question of how it is possible to have robust regulation despite the
observed heterogeneity within the nucleus.”
   Can gene regulation really depend on the fine details of this chaotic,
floppy, constantly jiggling tangle of chromatin? Won’t it be just a matter of
pure chance which parts of the genome happen to find themselves close to
one another at any instant? It looks like trying to pass on a super-important
message by sending the messenger and recipient to different stations on the
London Underground at rush hour, and hoping they just happen to bump
into and recognize one another as they make randomly chosen journeys.
![Fig. 5.3 A computer simulation of euchromatin. Each bead represents a single nucleosome: a disk of](media/fig-5.3.png)

Fig. 5.3 A computer simulation of euchromatin. Each bead represents a single nucleosome: a disk of
histone proteins wrapped around its edge with DNA. Image courtesy of Quinn MacPherson and
Andrew Spakowitz, Stanford University (see MacPherson et al. 2020).

   Yet cells turn out to have a way of imposing some control over the way
the chromatin threads are organized. They are marshaled into loops, rather
like those you might tug out of a ball of wool, that can be controllably
grown to bring distant regions into contact. A loop containing the enhancer
region needed to ramp up expression of a gene might thus be brought close
to the respective gene as the loop expands (fig. 5.4). Pairs or groups of
genes that are co-regulated by a shared enhancer (p. 73) might also be
brought together this way, allowing gene activity to be controlled in a well-
coordinated fashion.
   True, even this seems like a long shot: why should a given loop balloon
in the right direction and degree to bring the two target regions together?
That is still not well understood. “Even after forty years of studying this
stuff, I don’t think we have a clear idea of how that looping happens,” says
biochemist Robert Tjian. We’re not totally in the dark about it, though.
Each loop is formed by pinching two sections of a chromatin strand
together, binding them with a little hoop that acts like the lariat knot of a
lasso. This hoop can slide along the strand to make the loop grow or shrink
(fig. 5.5).

![Fig. 5.4 Enhancers distant from the gene they regulate (with a nearby promoter) are thought to be](media/fig-5.4.png)

Fig. 5.4 Enhancers distant from the gene they regulate (with a nearby promoter) are thought to be
brought into proximity via loops of chromatin.
![Fig. 5.5 How chromatin loops are regulated by cohesin and the protein CTCF.](media/fig-5.5.png)

Fig. 5.5 How chromatin loops are regulated by cohesin and the protein CTCF.

   The hoop is made of a cluster of four proteins, collectively called
cohesin. Cohesin has other important roles in the cell too: in particular, it
holds onto the pieces of chromosomes (called chromatids) as they separate
after replication when cells divide. Cohesin hoops attach the chromosomes
to the spindle of protein fibers on which this divvying up of genetic material
happens; that’s how the protein got its name.
   How big a loop is formed by this lasso-style sliding of the cohesin “knot”
depends partly on another protein, called CCCTC-binding factor or CTCF.
As the name indicates, this molecule is adept at latching onto DNA
segments that contain the sequence CCCTC—of which there are tens of
thousands throughout the genome, often near gene promoter sites. In
general, CTCF acts as a signal to stop sliding. In effect, it will let a loop
expand to expose the right enhancer, but tightens the knot to stop sliding
that would otherwise bring unwanted enhancers of other genes into the
loop. In this way, it acts as a so-called insulator, ensuring that only the right
enhancers for each gene are brought into play.
   However, as is so often the case in molecular biology, the story is not
quite this neat. In some situations, CTCF seems to activate other enhancers
rather than suppressing them. Regulation can also involve removing CTCF
to free the knot and allow chromatin loops to restructure. That seems to be
the job of a noncoding RNA molecule called Jpx RNA that is involved in X
inactivation (see p. 116). Jpx RNA can bind to DNA at the sites normally
occupied by CTCF, displacing the protein, which can then activate the Xist
RNA gene that is vital to inactivation. Without Jpx, X inactivation can’t
occur properly, a condition that is lethal for developing female embryos.
   Even once an enhancer-containing loop is formed, it’s no simple matter
to ensure that it comes close to the respective gene. The loops are floppy,
and there are typically tens of thousands of them that may form in
chromatin, so it’s still a crowded and bustling environment inside the
nucleus. And there is a dizzying array of other participants (fig. 5.6)—in
particular, promoter regions to which transcription factors will bind to boost
or suppress gene expression. Some transcription factors seem to work in
groups, often with other “assistant” molecules called cofactors. We
encountered one of them in the previous chapter: the protein TBP, which
binds to a region containing the sequence TATA (a TATA box) and helps the
RNA polymerase enzyme get underway (p. 177). A given gene might have
several promoters, both upstream and downstream, that regulate it in
different tissues or circumstances. And the enhancers may be accompanied
by insulators that prevent them from activating the wrong gene, as well as
so-called tethering elements that act as matchmakers for specific enhancer-
promoter partnerships. It looks, then, as though gene expression is regulated
not so much by switches as by committee. That complexity is what once
prompted researchers rather desperately to invoke complexes of many
molecules like that in fig. 5.2.
![Fig. 5.6 Some of the typical genomic elements involved in the transcriptional module of a metazoan](media/fig-5.6.png)

Fig. 5.6 Some of the typical genomic elements involved in the transcriptional module of a metazoan
gene.

   That there is a grand plan to all these executive decisions about gene
expression is clear when we take a look at the whole genome in the nucleus,
as mathematical biologist Erez Liebermann Aiden and coworkers did in
2014. They found that the chromatin seemed to be divided into six distinct
“compartments,” which were much the same in different human cell types.
Each compartment has a distinct network of “contacts” between different
parts of the chromatin—rather like different social networks—as well as a
distinct class of epigenetic marks, like friends who share the same tastes in
clothing. Each compartment contains many dense clusters of DNA and
other molecules, called topologically associating domains or TADs; the
fancy name really just means the different molecular components sit
together in the same spatial location. Within these TADs, the chromatin
regions contain around a million base pairs of DNA. This concept of TADs
echoes a proposal in 2002 by Dutch cell biologists Frank Grosveld and
Wouter de Laat that there are “chromatin hubs” in which active genes and
regulatory elements cluster to ensure robust and efficient transcriptional
regulation. Again, these features demonstrate that the three-dimensional
arrangement of chromatin somehow matters. It seems that “insulator”
control elements on DNA play a key role in partitioning this spatial
structure into TADs.
   It’s rather as if chromatin is a building with several floors
(compartments), each with many rooms (TADs) containing separate
committees. The committees have much the same membership in different
cell types, and also between human and mouse cells: it seems that there are
distinct groups of DNA, transcription factors and other molecules that are
inclined to gather together. But exactly where they gather—which room,
you might say—varies between one cell and the next. In this sense, says
Liebermann Aiden, a chromosome is like a snowflake, in that it has a
distinctive overall system of organization (like the hexagonal branches of a
snowflake) but no two are exactly alike in all their details.
   As mentioned, the sections of chromatin in the same TAD tend to have
the same epigenetic marks, especially on their histone proteins. It seems
that the histone modifications act rather like badges that tell each bit of
chromatin which committee to join. These particular epigenetic marks
appear to function, then, not as a signal to other molecules indicating
whether to bind and transcribe the DNA, but as designations for a higher
level of genome organization.

Ephemeral Committees
What do TADs really look like, and how do they work? The idea that these
regulatory committees are a kind of Lego-like assemblage of many
molecules seems rather implausible. That would be like assigning everyone
in a committee a specific place at the table and being unable to begin the
meeting until all are correctly seated. In that scenario, a rough estimate
suggests that it would take hours to get all the molecular members together
in the same room and seated in the right place, before any “decision” can be
made.
   And even this assumes that some members don’t drift away in the
meantime, as perpetually restless molecules are apt to do. In 2014 Robert
Tjian and his colleagues measured how long the components actually stay
bound to one another in a TAD, and found that this duration is only about
six seconds. “I was so shocked that it took me months to come to grips with
my own data,” says Tjian. “How could a low-concentration protein ever get
together with all its partners to trigger expression of a gene, when
everything is moving at this unbelievably rapid pace?” Evidently, the
committee needs to be very flexible. There might be no seating plan, nor
any requirement that all members are present, so long as they have a
quorum. The process may be literally rather fluid.
   The current idea is that, rather than forming a precisely structured
assembly, all these proteins, RNAs, and bits of looped DNA gather into a
kind of liquid blob enveloping the gene being regulated, which is distinct
from the watery liquid of the surrounding cytoplasm and has a high
concentration of transcription factors and other molecules required for
regulating the gene. We encountered such a situation in the previous chapter
in the formation of RNP granules (p. 170). I explained that it is a process
called liquid-liquid phase separation: each of the liquids constitutes a
different phase, meaning that it is a distinct (albeit here a composite)
substance that will not mix with the other.
   Phase separation is common and familiar in nonliving systems. It occurs
when ice starts to form in freezing water, and when bubbles of vapor pop
into being in boiling water. In those cases the phases are entirely different
states of matter: solid, liquid, or gas. But phase separation can also happen
between the same condensed (that is, liquid or solid) states, if the molecules
comprising them are sufficiently distinct—by which I mean that they much
prefer the company of those like them than of those in the other phase.2
   When gathered into these loose blobs—topologically associating
domains or chromatin hubs, also called “condensates”—the proteins can
repeatedly bind to and unbind from one another and from the DNA that the
blobs envelop, while remaining in the vicinity rather than diffusing away.
Instead of TAD formation relying on the highly unlikely chance encounter
of all the right molecules, these molecules have chemical properties that
make them likely to co-condense into a long-lived cluster. Their regulatory
work would then be a cooperative affair involving many repeated binding
events, rather like the committee reaching a decision through many
individual conversations among its members, even though they might never
manage all to sit down in the same room at the same time.
   Such a collective process fits with how many transcription factors are
nonspecific in their binding to DNA: they will stick more or less strongly to
various different sequences. As we saw, many of these proteins contain
floppy, intrinsically disordered parts of their polypeptide chains, which lend
a putty-like flexibility to their binding interactions. There are certainly
many places for them to stick: the ENCODE project identified more than
630,000 genomic regions that look like potential binding sites, comprising
about 8 percent of the entire human genome.
   What would make certain molecules, like transcription factors or
enhancer regions of DNA, apt to congregate while excluding other
molecules? Perhaps epigenetic markings such as those on histones could
tune a region of chromatin’s chemical nature to give it the required affinity;
maybe the disordered regions of transcription factors act as “sticky
patches”; perhaps long noncoding RNAs comprise a sort of scaffolding that
interacts with some of the components of the condensate and holds them all
together; perhaps it’s a bit of all of these. No one is really sure yet. One
problem is that the mixture of components inside cells is so diverse and so
complex that it is hard to develop theoretical models of such putative liquid
droplets in the way one can for simple liquid mixtures like oil and water.
   This picture of gene regulation via the formation of liquid droplets is
very appealing because it could explain how a protein that has a very low
concentration in the cell as a whole might develop a locally high
concentration at the gene it is supposed to regulate. But good evidence for
droplets forming amid the tangled mass of chromatin in the cell nucleus is
difficult to find. Such droplets have been seen in lab experiments on
mixtures of biomolecules in test tubes, but those don’t necessarily reflect
the physiological conditions in a live cell. Besides, is it really such a good
idea for cells to convene stable liquid droplets to induce gene regulation,
which typically has to be turned on and off quickly? How would you
disperse a droplet once it formed?
   Maybe the condensates aren’t persistent blobs, but more transient and
dynamic: Tjian and his colleague Xavier Darzacq prefer to call them, more
neutrally, “hubs.” Darzacq and his coworkers have explored how these hubs
or condensates—call them what you will—form from transcription factors
called Bicoid and Zelda that kick off the very early developmental stages of
fruit fly embryos. Zelda is a so-called pioneer TF that “recruits”3 other TFs
to bind chromatin and activate genes. You could say it’s like the person who
calls the committee meeting. Like many TFs, it is full of disordered regions.
   The researchers followed the trajectories of individual protein molecules
in fly embryos, which they could see in a microscope after giving the
proteins tags that glowed like fluorescent bulbs under light. They found
that, while the switch in an embryo’s state that these TFs induce takes
several minutes to occur, Zelda and Bicoid bind to chromatin only for a few
seconds before detaching. These proteins seem to form hubs that are
constantly changing in size and shape, like a swarm of bees buzzing around
a hive. The hubs act as a focal point to concentrate other proteins so that
they make brief but repeated contact with DNA, somehow collectively
triggering a switch in gene activity and consequently in the state of the
cells.

Structure for Free
Whether or not liquid-liquid phase separation—that’s to say, droplet
formation—is involved in gene regulation, it seems clear that cells do use it
in other ways, for it offers “structure for free.” We’ve seen that cells contain
compartments called organelles in which various processes happen
essentially in isolation from the rest of the cell: energy generation in
mitochondria, say, or the processing and packaging of proteins in an
organelle called the Golgi apparatus, or the breaking apart of worn-out
molecules or pieces of invading entities like viruses within lysosome
organelles. Each of these structures needs to have enzymes dedicated to
their construction, which is expensive in parts, labor, and time. But droplets
formed by phase separation can appear spontaneously and quickly once
their constituents are present in sufficient concentration, and can be
dispersed once they have done their job. They can, then, act as ephemeral
organelles for organizing cell processes, produced by physical forces alone
rather than by genetic specification. “Far from being the peculiarity it once
was,” Tjian and his colleagues have written, “phase separation now has
become, for many, the default explanation to rationalize the remarkable way
in which a cell achieves various types of compartmentalization.”
   For example, in 2009 Clifford Brangwynne, working as a postdoc with
biophysicist Tony Hyman at the Max Planck Institute of Molecular Cell
Biology in Dresden, reported that dense structures called P granules, which
contain proteins and RNA and form within germ cells, are liquid droplets.
“After that, I wanted to know if this idea of liquid states of condensed
biomolecules was general or not,” says Brangwynne, now at Princeton
University. He started looking at the nucleolus—the region in the nucleus
where protein-manufacturing ribosomes are made—and found that it too
had all the hallmarks of a liquid droplet. As with the case of RNP stress
granules, such temporary compartments could act as storage vessels—for
example to keep concentrations of cell constituents steady even while the
rate of gene expression undergoes inevitable random fluctuations. When
there is over-expression, the excess can be mopped up within a droplet;
when there is under-expression, some of the stored molecules can be
released.
   The three-dimensional structure of chromatin itself might be partly
organized this way. The tangled mass we saw earlier typically contains
especially dense, almost solid-like regions called heterochromatin,
dispersed within the more open euchromatin. While euchromatin is
accessible to the molecules that activate and transcribe genes,
heterochromatin tends to lock the DNA away so that it is silenced. This
segregation of regions of different density looks like phase separation—
controlled, perhaps, by the nature of the epigenetic marks on chromatin
itself. Brangwynne suspects too that the fibrous tangles of intrinsically
disordered proteins underlying neurodegenerative diseases such as
Alzheimer’s (p. 164) might begin as liquid droplets. If that’s so, blocking
the condensation process might avert the disease. “Liquid phase
condensation increasingly appears to be a fundamental mechanism for
organizing intracellular space,” write Brangwynne and his Princeton
colleague Yongdae Shin. Rather than building and controlling everything
from the ground up starting with information in the genes, cells apparently
have the wisdom to accept and exploit the order that the laws of physics and
chemistry offer them for free.
   Whatever their exact nature, transcription hubs show biology working at
the molecular level in a very different way to the conventional picture of
precise and specific molecular interactions directing cell processes like
pieces of clockwork. “Many of the textbooks and even our language
conveys this kind of factory-floor image of what goes on inside of a cell,”
says Brangwynne. “But the reality is that the computational logic
underlying life is much more soft, wet and stochastic than anyone
appreciates.” The molecular decisions are made by rather ad hoc
committees consisting (or so it might seem) of whoever happens to be
around. Hyman has compared them to flash mobs: they congregate when
the music is on and disperse when it stops.
    They might be involved not just in the regular operation of cells but in
pathological states too. Biophysicist Rohit Pappu believes that mutations of
the gene HTT, implicated in Huntington’s disease (which is ultimately fatal
and currently incurable), cause the protein it encodes (huntingtin) to
become sticky and form condensate-like tangles. Huntingtin has disordered
regions and can adopt several different conformations and interact with a
wide range of others. It is somewhat archetypically promiscuous and
“sticky,” involved in a variety of processes in the body, and produced in
many different tissues, although it is in the brain that the mutant form
manifests its terrible consequences. Pappu thinks that disordered proteins
like this with sticky patches can act as seeds for condensate formation. In
this view, the role a protein takes may depend on its context: what is sticky
to some proteins might not be so to others.
    Disordered proteins, with their propensity to form many indiscriminate
and transient interactions with other molecules, seem to be ideally suited for
promoting condensates. That’s a useful property for cells, since it is now
clear that these “membraneless compartments” have a wide variety of
functions. But such versatility apparently comes at a cost, for such
intrinsically disordered proteins also have a tendency to aggregate, like
prion proteins and huntingtin, into clumps and tangles that can be toxic for
cells. Our cells seemingly walk a tightrope, and we must presume that
natural selection has found the benefits of condensate-forming disordered
proteins to generally outweigh the drawbacks.
    All the same, that life might make use of effects like this is disconcerting
for some biologists. It seems to put a disturbing amount of control in the
hands of processes that seem too messy and vague, too analog and
contingent—and in consequence, hard to entrust with the important task of
directing the cell. What’s the point of loading all that digitally precise
information into the sequences of DNA, RNA, and proteins if you end up
relying on vague molecular affinities and floppy, ill-defined structures?
    It’s a good question, and cuts to the core of why we need new narratives
for how life works. At first glance, there’s a real puzzle here. Why give
molecules such precise information encoded in their atomic-scale structure
if it’s only going to be read out in a hazy environment? It’s like telling each
committee member exactly who they may talk to and what they may say,
only to then create extremely lax rules for who comes to the meetings, how
long they stay, and so on.
   But with closer thought, such flexibility and vagueness of instructions is
exactly what might be expected to work well. What are the chances of
getting a good committee decision if each member is so constrained in what
they can do and say? What’s more, the decision-making process needs a
range of skills and behaviors. Sure, you want some folks to arrive at the
table with precise and specific information: the treasurer with the accounts,
say. But a good decision also needs generalists and experts in broad areas. It
needs individuals who are good at connecting others and reconciling their
points of view.
   In any case, many committees are tasked not with coming up with some
extremely detailed action plan that demands strict adherence to every point,
regardless of whether it fits the specific context, but rather, with finding
broad strategies or with making blunt binary decisions based on a range of
detailed inputs: yes or no? This, in fact, is very much what life is like as we
ascend through the hierarchy of its mechanisms. The need is for reliable
generic decisions amid a tremendous diversity of experience and
circumstance. This typically demands that lots of details be weighed,
filtered, and integrated.
   In the end, what we are talking about here is the management of
information: how it flows, how it is combined and integrated, and how it
copes with the unexpected. If life’s informational schemes are
overspecified, their outputs are liable to be brittle: too fine-tuned to
withstand variations and noise. What’s required instead is robustness—
which in general demands adaptability and flexibility. It requires not a
concentration but a dispersal of power. Gene regulation by condensate hubs
might be influenced at several levels: for example via changes to the
segregating propensity of proteins (by transcriptional control of alternative
splicing) or of chromatin (by epigenetic markings to DNA and histones), or
via changes to expression levels that alter the mix of RNA and proteins in
the nucleus, or via the transcription of particular noncoding RNAs. Genes
themselves play a role in such things, but it’s not obviously meaningful to
ask who is ultimately in control. The process works as an integrated whole.
Combinations
Changes in gene regulation can be triggered by signals coming from outside
the cell’s nucleus, and indeed outside the cell itself: the arrival of a hormone
in the bloodstream, say (which might induce a cascade of kinase activity),
or developmental signals from surrounding tissues (a process considered in
the next two chapters). These messages are conveyed through networks of
interacting proteins in the cytoplasm. Likewise, protein networks interpret
and respond to the messages coming in the other direction: from the
nucleus, in the form of altered expression levels of genes. The “signaling”
goes both ways.
   Or rather, it goes all ways. Bear in mind that the very notion of a “signal”
is clearly a metaphor borrowed from electrical engineering, with the
implication that it travels down some pathway to trigger a process at the far
end, perhaps in the digital on/off manner of a light switch. There’s some
value in that image, but still it’s a metaphor. Life is elsewhere. What
biologists call signaling, says developmental biologist Alfonso Martinez
Arias, doesn’t just (or even primarily) activate or suppress gene expression,
but “tends to shake the whole of the activity of the cell”—it can alter
metabolism, cell adhesion, the internal traffic of molecular packages, and so
on.
   Just as gene regulation is better seen not as a series of switching
operations in a fixed circuit but as a more fluid and collective process of
consensus-reaching among many molecules, so the signaling within protein
interaction networks no longer appears to have a precise “digital” logic to it,
but follows principles that seem uniquely biological. Let’s take a look at an
example.
   Earlier I mentioned that one of the classic misnomers of genetic
terminology was the gene called BMP, which encodes a protein named
bone morphogenetic protein. It is so named because it was found in the
1960s that this protein, introduced to the body in the wrong places at the
wrong time, could trigger the formation of bone where bone did not belong.
Two decades later it was found that there are several types of BMP protein,
and that they can cause stem cells in the early embryo to develop into bone-
and cartilage-forming cells. BMPs are themselves members of a larger
family of proteins called transforming growth factor β (TGF-β) proteins
which have a broad range of developmental effects: they are examples of
so-called morphogens (“shape-formers”), which influence the
differentiation and arrangements of embryonic cells and tissues.
   One type of BMP, for example, is involved in the patterning called
gastrulation, which happens in human development around fourteen days
after fertilization. This is when the embryonic stem cells start to specialize
into different tissue types, and the embryo proper begins to acquire a real
shape rather than just being a clump of cells. Other BMPs guide later tissue
growth too: they are expressed, for example, in bone, cartilage, kidney, eye,
and early brain tissue, and are involved in wound repair and the reshaping
of blood vessel networks. They are a classic example of why it is
meaningless to attempt to say what some proteins “do”: the “meaning” of a
BMP protein for the organism depends on when and where it is expressed.
It’s a messenger, not a message.
   Another way to say it is that BMPs are key hubs in protein networks:
nodes through which several signals are routed that direct cell behavior and
fate in one way or another. The pathways mediated by BMPs begin at the
surface of a cell, where these proteins bind to receptor proteins spanning the
membrane, changing the receptor shape allosterically in a way that registers
the binding event at the other end of the receptor, on the inside surface of
the membrane (fig. 5.7). This change in turn is registered by proteins called
Smads, which convey the signal to the nucleus. Here they interact with
other molecules to switch certain genes on or off (they are, in other words,
transcription factors), initiating a response of the whole cell to the signal
that arrived at its surface. Different BMPs—there are eleven or so for
mammals, each encoded by a different gene—can bind to the receptors and
convey different signals. Because the binding of BMPs to BMP receptors
can be altered by other molecules, the BMP pathway can interact with other
pathways to create crosstalk between cells during development.
![Fig. 5.7 How BMP proteins take part in cell signaling. The binding of a BMP to its receptor protein](media/fig-5.7.png)

Fig. 5.7 How BMP proteins take part in cell signaling. The binding of a BMP to its receptor protein
in a cell membrane triggers phosphorylation of (i.e., addition of phosphoryl, P, to) a protein called a
Smad on the other side of the membrane. This modified Smad, in combination with other varieties of
Smad proteins, can then regulate the expression of a gene in the nucleus.

   Each BMP has a different chemical structure: a different sequence of
amino acids in its folded-up chain. What’s more, both BMPs and their
receptor proteins are made from more than one distinct protein molecule.
BMPs themselves are pairs (called dimers), while their receptors typically
have four component parts. And it’s not simply the case that each BMP
dimer has a designated receptor to which it binds like a lock and key. These
molecules aren’t terribly choosy: each BMP dimer might stick to several
different combinations of receptor subunits, with varying degrees of avidity.
It’s a combinatorial system, in which the components can be assembled in
many ways (fig. 5.8): less like locks and keys, more like Lego bricks. The
possible permutations are exhausting even to contemplate. So how can the
BMP pathway ever deliver a specific message to guide a cell’s fate? It looks
rather like trying to get a message through an old-fashioned telephone
network when the operators are just plugging in the leads at random. Who
knows what will emerge?
   Yet although they are not highly selective, the various BMPs do have
preferences for certain receptors. In 2020 Michael Elowitz and his
coworkers set out to understand the rules of this important signaling hub.
They began by characterizing the various possible combinations, looking at
the binding propensities between ten major mammalian forms of BMPs and
seven receptor subunits (all in mouse cells). That meant studying a lot of
combinations, but it was made possible with an automated robotic system
for carrying out the reactions in cell cultures.
![Fig. 5.8 In the combinatorial BMP signaling pathway, different BMPs can dock into different](media/fig-5.8.png)

Fig. 5.8 In the combinatorial BMP signaling pathway, different BMPs can dock into different
receptors, and different combinations will have various effects on the cells. Here, for simplicity, I
show each BMP as a single entity and the receptors as pairs of subunits; in reality each of those
entities is itself a dimeric (two-part) protein assemblage.

   The researchers deduced the preferences from the strength of the “output
signal”: the activating effect on Smad proteins inside the cells. They
engineered the mouse cells so that the Smads would turn on a gene that
encodes a yellow fluorescent protein. The output signal for a given set of
BMPs and receptor subunits was then gauged from the easily monitored
measure of how brightly the cells fluoresced. It was like activating a slot
machine by putting a BMP coin (of which there are ten types) and two
receptor coins (seven types) into three slots, and seeing what the machines
does in response.
   The interactions, although promiscuous, were far from “anything goes.”
There were definite rules about the effects that different BMP/receptor
combinations had. For example, certain BMPs have much the same effect
as one another and are interchangeable, while others do not. One BMP plus
two receptor subunits might, for example, work as well as an assembly of
three entirely different components. Or one assembly might tolerate the
swapping of one specific BMP for another, so long as the receptor stays the
same. Sometimes two swapped components might have independent
effects, so that their combined effect is a simple sum. Sometimes, in
contrast, the effects might mutually reinforce each other, or cancel out.
   In general the BMPs could be grouped according to whether they will
have the same effect in a given context, such as a certain cell type. The
researchers looked at two types of cell: epithelial (organ lining) cells from
mouse mammary glands, and mouse embryonic stem cells. They found that,
say, a pair of BMPs might substitute for each other in one type of cell but
not in another. It’s a little like the way you can substitute the word right for
correct and still retain the same meaning in the context of the sentence
“That’s the right answer,” but not “That’s my right hand.”
   This would explain why the biological effect of a given BMP has been
seen previously to differ in different tissues. For example, the protein
denoted BMP9 can substitute for BMP10 in the BMP pathway that leads to
formation of blood vessel networks, but not in the pathway involved in
heart development. Such context dependence is hard to reconcile with the
idea that molecular communication depends on highly selective recognition
and binding processes—in which case, either you have the right match or
you don’t.
   Why does BMP signaling work in this apparently complicated way, in
which the signal can use many different inputs, sometimes interchangeably
and sometimes not? Elowitz’s team thinks that the answer is that it gives
you more for less. If there’s only one way a given component (such as a
BMP) can work—if you have to give it the right pair of receptor subunits or
else it does nothing—then there are only a few combinations of the
elements that will function. But if every element is equivalent, there’s no
control—you’re always likely to have some components that will work, so
it might be impossible to turn the signal down or off. With a combinatorial
system you have many more options that will do the job, while retaining
distinctions of use and meaning. It’s a little like the way languages work:
there’s nearly always more than one combination of words that will convey
much the same meaning, but those combinations aren’t arbitrary. In many
particular contexts, some choices work better—convey a clearer or more
emphatic meaning—than others.
   One advantage of such combinatorial diversity of outputs is that it allows
the molecules to convey distinct messages to a wider variety of cell types—
and so, in a developing tissue, to produce more complex patterning with a
small repertoire of signaling molecules. One group of cells in the
developing embryo could be assigned to becoming cartilage, say; another
group to bone; and others to other fates.
   The many possible combinations might create some fuzziness in the
criteria for whether a cell adopts one fate or another. But the researchers
think this might be sharpened by operating in conjunction with other
signaling systems—a bit like the way the meaning of a sentence can be
sharpened by the context created by others that precede and follow it. In
particular, a pathway involving the Wnt family of proteins (see p. 77) is
similarly central to early development, and seems often to operate alongside
BMP signaling. Sometimes the pathways antagonize one another (for
example, Wnt proteins suppress the effects of BMPs); sometimes they
enhance each other. The Wnt pathway might follow similar combinatorial
rules, although that’s yet to be tested experimentally.
   Molecular promiscuity is, however, also a trick that pathogens can
exploit. For example, adenoviruses—a group of viruses that can cause the
common cold—produce a family of proteins collectively denoted E1A,
which disrupt the host’s defense mechanisms. E1A proteins are intrinsically
disordered, giving them the ability to bind to a variety of regulatory proteins
in human cells, including the p53 protein that regulates the cell cycle and is
implicated in many cancers. By doing so, E1A proteins can interfere with
the cell cycle of infected cells, preventing them from undergoing the
programmed death (“apoptosis”) that would stop the virus from replicating.
By throwing a wrench in the regulatory works, this strategy can have some
serious secondary effects: cultured mammalian cells can turn cancerous
when infected with adenoviruses.

The Benefits of Promiscuity
Elowitz and his colleagues think that the combinatorial and promiscuous
molecular signaling used in the BMP pathway might represent a widespread
design principle of the molecular wiring of cells. “Just as neurons wired
together through axons and dendrites can perform complex information
processing,” Elowitz says, “so too can proteins wired together through
biochemical interactions.” His postdoc James Linton draws a loose parallel
with the olfactory system that determines smell. For humans there are
around four hundred receptor proteins lining the membranes of the
olfactory bulb in the nose, which together can discriminate between a vast
number of (one estimate puts it at one trillion) odors. That range simply
wouldn’t be possible if each odorant molecule had to be uniquely
recognized by its own dedicated receptor. Instead, the receptors seem to
bind odorants somewhat promiscuously with different affinities, and the
output signal sent to the brain’s smell center is then determined by
combinatorial rules. Perhaps the most useful analogies for how cells work
are themselves biological, such as olfaction or cognition. Maybe the only
way to truly understand life is with reference to itself.
   It’s possible that making promiscuous, reconfigurable networks doesn’t
just convey advantages but perhaps is the only way a complicated system
like our cells can work, if it is to be robust against ineluctable randomness
and unpredictability in the fine details. The operational principles
exemplified by gene-regulating condensates and signaling pathways like the
BMP system—with their molecular promiscuity, their combinatorial, fuzzy
logic, their versatility for addressing and promoting many different cell
states, and their apparent evolvability—may well be a sine qua non for
multicellular organisms in which genetically identical cells work together in
diverse, specialized states. This principle might even have been the
innovation that allowed beings like humans to emerge. Such insensitivity to
fine details is, after all, a much wider aspect of how large, multicellular
organisms work: you can see it in the operation of the brain’s neural
networks, the way cells assemble into tissues and the ability to
accommodate gene mutations and deletions. It looks like an effective
general strategy for robustness.
   Cellular systems are, after all, very noisy. Molecular encounters in this
crowded, jostling environment are very much a matter of chance, and there
are also random fluctuations in the number of different proteins that get
produced from moment to moment. That’s one reason the cell’s wiring can’t
be compared to the complex electronic circuits in a laptop: no two cells are
ever in wholly identical states at any given moment, even when they are
both ostensibly doing the same job, such as acting as muscle or kidney
cells. A cell in which each component is wired specifically to another
would be highly vulnerable to such uncontrollable variability. It would be
as though circuit elements keep dropping randomly in and out of the
network. What’s more, every time a cell divides, there’s no guarantee that
exactly the same circuit gets reproduced, because of random copying errors
in DNA replication. If successful functioning depends on getting the
network wiring just so, any mutations are likely to derail the whole affair.
Combinatorial logic, on the other hand, has a certain amount of sloppiness
that can absorb (and even exploit!) such variation.
   Biological systems generally have this robustness: as we saw earlier, if
we disable a gene that looks at face value to be critical to survival, often the
organism barely seems to notice. It will readjust the interactions and
pathways in its gene and protein networks to compensate. The redundancy
and the compensatory function of proteins in a family, as illustrated by the
BMP system, might be a key part of that ability.
   These promiscuous, highly interconnected protein networks also promote
the ability of the organism to acquire useful new capacities by evolution. “A
system that has higher connectivity tends to evolve new functions more
easily, as deleterious mutations [of the component parts] can be better
tolerated,” says biologist Meng Zhu. Evolutionary biologist Andreas
Wagner and his student Joshua Payne have shown that the promiscuous
binding of transcription factors can indeed promote both robustness to
mutations and the ability to evolve. If there’s slack in the system—say,
because promiscuous binding allows one protein to substitute for another—
it’s possible for the network to develop new functions without losing old
ones.
   It seems likely that metazoans have evolved this evolvability. One of the
odd features of transcription factors that bind to DNA is that, in eukaryotes,
the base sequences that they recognize are often surprisingly short—
perhaps six or so base pairs long. This compromises the selectivity of their
binding, because, if you pick a six-base sequence at random, it’s likely that
you’ll find a lot of copies throughout the genome. But there’s no reason the
selectivity has to be this approximate; in prokaryotes the binding sites are
longer and the binding is therefore more specific. It seems that eukaryotes
have, so to speak, chosen this sloppiness—probably because it allows new
regulatory pathways to develop, opening up the potential for variation and
evolvability. Once again, we see that E. coli is not like the elephant. The
clean and elegant mechanism of gene regulation found in E. coli’s lac
operon (p. 114) is not, in general, a good model for how metazoans regulate
their metabolism, which tends to be much less simple. Cell biologist Marc
Kirschner suggests that building mechanisms that permit evolvability into
the molecular pathways of the cell may be far more important for large
animals than for bacteria, because they have much smaller populations and
so can’t rely simply on a lucky mutation arising in a vast number of
offspring.4
   In short, then, much of the cell’s biochemistry might be far less sensitive
to the fine details than has been thought. It’s not exactly that details don’t
matter—but that we can’t easily tell a priori which do and which don’t.
That, in a nutshell, might be said to be the central challenge of molecular
biology. With so much detail at the molecular level, it’s tempting to suppose
that all of it is crucial to what happens at higher levels. But as gene
knockout experiments show, often it isn’t. Again, what matters is not how
each member of a molecular committee made its deliberations, but the
collective decision that emerges. The apparent chaos of interacting
components is in fact a sophisticated system that can process and extract
information reliably and efficiently from complicated and contingent
cocktails of signaling molecules.
   Understanding the combinatorial logic of cells should allow us to control
them with much greater specificity. There could be important implications
for drug development, for example. One of the challenges in ordinary
medicine is that drugs can be highly specific for a target protein, but that
target protein may be nonspecific in terms of the cell types in which it is
expressed. In other words, you might be able to hit the protein target very
accurately, but not know for sure what effect that will have in different
tissues—or whether it will have any effect at all. The cell’s combinatorial
logic suggests that drugs might need to be more sophisticated than single-
molecule “magic bullets”: they may have to hit different combinations of
tissue-specific targets to induce the desired response.
Emergence
Research into complex systems has suggested how best to think more
broadly about these operational principles of molecular and cell biology:
the goal of these principles is to take causation largely out of the hands of
the molecules themselves. To reliably produce some larger-scale response,
whether it be the fate of a given cell, the cellular collaborations that make
tissues and organs, or an organism’s behavioral reaction to a stimulus, it is
preferable to match the scale of the cause to the scale of the effect. Complex
organisms seem wired to enable this so-called causal emergence.
Emergence refers to the appearance of overall behavior in a complex
system of many parts that can’t be predicted or understood by focusing just
on what those parts themselves are like. That such phenomena occur is
beyond doubt. You’ll never fully understand the flocking behavior—called
a murmuration—of starlings by probing the workings of the avian mind at
the neuronal level, nor will a detailed analysis of car mechanics enable you
to decipher how traffic jams form (fig. 5.9).
   Some researchers, though, are suspicious of this notion of emergence. It
seems to them an appeal to quasi-mysticism, as though a magic ingredient
has been added to the system beyond the forces and exchanges of matter
and energy between its constituents. They might assert that everything the
system does can still be understood from a bottom-up dissection, given
enough computational power to put all the pieces together.
   But the idea of causal emergence doesn’t deny that a system can be
dissected into its constituent elements, nor does it require anything to be
added to their interactions. Rather, it asserts that we can’t speak of the cause
of the large-scale behavior as originating primarily among those microscale
interactions. To talk about causes in a meaningful sense, we have to
acknowledge that there are higher-level entities and influences that must be
recognized as every bit as real and fundamental as their constituent parts,
and not just as arbitrary ways to aggregate them. These are the causes of
what transpires—and they are not just the sum of lots of microcauses.
![Fig. 5.9 Emergence refers to the appearance of behaviors or outcomes in complex systems that can’t](media/fig-5.9.png)

Fig. 5.9 Emergence refers to the appearance of behaviors or outcomes in complex systems that can’t
be understood purely from a study (however exhaustive) of their component elements. It can be seen,
for example, in the flocking of birds and the appearance of traffic jams. Images: Shutterstock.

   We already sense intuitively that some phenomena have this nature. We
recognize that we humans are causal agents in our own right. My neurons
are in no meaningful sense the real authors of this book. They are what
(among other things) enable it to be written, and it is certainly true that
aspects of its composition, such as my ability to deploy syntax and
grammar, can be attributed to specific brain circuits. But beyond a certain
level of reductive analysis, any notion of a true cause for the macroscale
event of this book’s composition starts to disappear. There is certainly no
meaningful notion of authorship, of ideas and motivations, among the
protons and electrons of my body. By the same token, neurons are
themselves real entities too, and need to be posited as such to understand
the brain. They are not arbitrary divisions of a cloud of fundamental
particles.
   Yet causal emergence has been a challenging concept to pin down
scientifically. “Most [scientists] agree that there is causation at the macro
level,” says neuroscientist Larissa Albantakis, “but they also insist that all
the macroscale causation is fully reducible to the microscale causation.”
This is the reductionist view: all causation flows up from the lowest levels.
How can we know if that’s true or not?
   Many different approaches have been suggested to try to quantify
causation: to identify not just how a complex system behaves but to what
the behavior can be attributed. Yet neuroscientists Renzo Comolatti and
Erik Hoel have shown that more than a dozen such measures of causation
all reveal that in some complex systems it may indeed arise primarily from
higher levels of organization in an emergent manner. That’s to say, the
“causal power” among the microscale elements is negligible; it resides
mostly within the larger-scale structures they form. It would seem most
unlikely that all these measures, developed in fields as diverse as
neuroscience, economics, and philosophy, are somehow mistaken and
misattribute where causation happens.
   What such examples of causal emergence share, according to Hoel, is
noise reduction—by which he means independence of the outcome on
random fluctuations or chance events at the microscopic level. The response
of a cell to a particular external signal can’t afford to be contingent on
whether a particular protein is present in the right location at the right time
in the right concentration, just as the response of an entire organism can’t,
in general, hinge on a specific neuron in the brain firing at the right
moment. It therefore makes perfect sense that evolution would “design”
complex organisms to display causal emergence: to fit the scale of the
causes to that of the effects. Biological systems thereby become more
robust not just against noise but also against attacks. “If a biologist could
figure out what to do with a [genetic or protein] wiring diagram, so could a
virus,” says Hoel. Causal emergence makes the causes of behavior cryptic
at the microscopic scale, hiding it from pathogens that can only latch onto
particular molecules.
   This is not to say that all causation in complex organisms is emergent.
Evidently, single-gene mutations can have a significant impact on a
phenotype, and a drug that hits a specific protein can sometimes disrupt a
physiological response. Evolution doesn’t so much shift all causation to
higher levels as spread it among the various levels. We might anticipate that
there are reasons why more or less emergence is best for a given process—
but if so, we don’t know in general what they are.
   While causal emergence seems to be a general design principle for life, it
is rarely evident in our own technologies. Machines tend instead to use
simple chains of causation: this cog turns that one. Remove a cog and the
machine stops. Arguably something more emergent is now evident in
computing technologies. We tend (rightly) to imagine that the causal
explanation for what happens on our screens is to be found in the
algorithms and machine code used to program them, rather than in the
disposition of electrons in transistors. But it’s striking how some efforts to
improve computing, particularly to create more versatile and powerful
artificial intelligence, focus on making it more like our own neural circuitry,
whether that is by using so-called artificial neural networks for machine
learning, producing “neuromorphic” circuitry that can reconfigure itself like
our brains, or giving advanced AI human-like attributes such as internal
representations of the world. In other words, maybe the better computers of
the future will be more causally emergent.
   If there’s a human technology that really does resemble how life works in
the causal sense, perhaps it is again the “organic technology” of language,
in which meaning and indeed causal power—the ability to induce thought,
mood, action—increase as we go up the scale from letters (or phonemes) to
words, sentence, paragraphs, and so forth. Zoom in on a text’s component
characters and you lose all meaning: the characters themselves are not only
effectless but have no intrinsic function.
   The key reason causal emergence seems to be so widespread in how life
works is, then, that this is how to “engineer” with noisy components. If you
are making a machine from chunky, precision-milled cogs, you don’t need
causal emergence, because the parts can be relied on: cogs don’t go
wandering randomly out of place. But molecules do! Perhaps causal
emergence isn’t the only way to tame stochastic systems like this, but no
one has yet identified any other.

The Emergence of Multicellularity
In collaboration with other researchers, Hoel has investigated how and
where causal emergence arises in the networks of protein interactions (the
interactomes) of a wide range of organisms. The group looked at around
1,500 species of bacteria, 11 of archaea (the other major group of single-
celled prokaryotic life), and 190 of eukaryotes including humans and other
mammals. Using a measure called “effective information” to quantify
causation, the researchers searched for “informative macroscales” in the
networks—situations where a group or cluster of protein-protein
interactions could be replaced by a single “macro-node” in the network that
does the same job as the collective. Such macro-nodes can be considered
autonomous units in producing the observed outcome at the level of the
phenotype. It’s a bit like dividing up a population geographically into cities
and towns: these are not just arbitrary groupings, but “real things” with
discrete and identifiable influences. These macro-nodes will function
reliably even if there’s some variability or noise among their component
parts. They become genuine causal entities that operate at a higher level of
organization: agents of causal emergence.
   Hoel and colleagues found that there was significantly more causal
emergence—more informative macroscales—for eukaryotes than for
prokaryotes (fig. 5.10). In effect, the more complex multicellular organisms
that appear later in evolutionary history tend to assign causal roles to higher
levels of organization in their networks. In this way, these organisms can
tolerate more noise and indeterminism in the microscales, because those
scales aren’t the primary determinant of phenotypic outcomes such as body
shapes and behaviors.
   Did this shift from primarily microscale to higher-level causation in
interactome networks result from the switch to multicellularity—or did it
enable that? The question is difficult to answer, because the real evidence
lies way back in evolutionary time when multicellularity first emerged.
However, we can get some clues from looking at species today that exist at
the borderline of unicellularity and multicellularity. For example, Spanish
evolutionary biologist Iñaki Ruiz-Trillo and his coworkers have studied the
genome of a single-celled eukaryote called Capsaspora owczarzaki, one of
the closest evolutionary relatives of the first multicellular animals, such as
sponges and the marine organisms called cnidarians and ctenophores.
![Fig. 5.10 Causal emergence is more evident in eukaryotes, especially multicellular complex](media/fig-5.10.png)

Fig. 5.10 Causal emergence is more evident in eukaryotes, especially multicellular complex
organisms, than in prokaryotes. In other words, evolution produces “causal spreading,” in which
causation is increasingly conferred on higher organization levels. This graph is a so-called violin plot,
where the width of the bands shows how many data points there are at each value on the y-axis.

   Capsaspora has more genes involved in regulatory functions (generally
by encoding transcription factors) than any other known single-celled
organism. Ruiz-Trillo and colleagues discovered that the networks that
these transcriptions factors govern are often found too in animals: the
networks were already “primed and ready to go” before true multicellularity
took off. This is perhaps not surprising given that single-celled organisms
like this (such as amoebas) can already show multicellular cooperation at
certain stages of their life cycle, being able to aggregate into temporary
collectives that look somewhat like “improvised animals.”
   Gene and protein networks linked via transcription factors are, however,
only one way in which gene regulation works. We saw, for example, that
regulation in animals is often carried out by long noncoding RNA
molecules—and Capsaspora has an abundance of these too. Regulation is
also managed by changes to the way chromatin is packaged, and by the
coming together (in ways that are still not fully understood) of a gene with
enhancer elements on some distant part of the chromosome. But
Capsaspora doesn’t have remote enhancers, suggesting that perhaps these
were what enabled organisms to progress beyond loose collaborations of
autonomous cells to become permanent multicellular assemblies. The
regulatory promoter sites in Capsaspora tend to be close to the respective
genes, and only a few proteins congregate in the regulatory complexes, in
contrast to the rich variety of proteins and other molecules that turn up
(perhaps as liquid-like condensates) in the clusters involved in our own
regulatory processes.5 Ruiz-Trillo and colleagues think that those latter,
very complex structures might have been made possible with the advent of
enzymes that can reshape and reorganize chromatin—enabling a wider
variety of interactions within the genome and thereby expanding the
combinatorial possibilities for this interacting with that.
   The switch to multicellularity seems, then, to involve the appearance not
of more primary genetic resources—more or different genes—but of new
ways to regulate them. “Much of the innovation in gene content seen in the
transition to multicellularity,” say Ruiz-Trillo and colleagues, “is rooted in
pervasive ‘tinkering’ with pre-existing gene families”—that idea again! The
tinkering might, for example, generate new transcription-factor proteins
from existing domains (p. 172), which could produce new linkages in the
networks. It could also engender new ways for gene regulation to respond
to signals from outside the cell, thanks to the appearance of proteins that
help cells stick together and that can receive and pass on signals from
molecules outside the cell membrane.
   The default assumption for such changes is that they were driven by
natural selection. That’s to say, some random mutation gave a cell lineage a
new regulatory function which conferred some reproductive advantage, and
off it went. But that’s not the only possibility. Even rather profound changes
in the complexity of organisms, such as a transition to multicellularity
enabled by new regulatory mechanisms, might not be a product of
Darwinian natural selection at all. Although it is commonly assumed that
“evolution” and “natural selection” are synonymous (perhaps because many
popularizations imply or even state as much), this is not the case; there are
other drivers of evolutionary change too.
   Ultimately such “non-Darwinian” changes also tend to arise from random
genomic mutations. These can become fixed in populations not by selection
but just by sheer chance: organisms that contain a given mutation just
happen to survive, and not because they are best adapted. This process,
called random genetic drift, is especially salient in small populations, where
survival may be more of a lottery: there’s a greater chance that the “fittest”6
organisms might simply have an unlucky encounter with a predator. If a
mutation does not make any difference to fitness—if it is “neutral,” or
indeed even if it is only very slightly disadvantageous—then it might stick
around anyway, because there’s no strong pressure on natural selection to
weed it out. Indeed, most biologists reject the idea that every feature of an
organism is adaptive, the result of rigorous selection. For example, the
microscopic marine organisms called radiolarians grow a great variety of
intricately shaped mineral exoskeletons, and each separate species has its
own distinctive shape. But it’s quite likely that one shape is as good as any
other, and that the differences between species are due to random drift
rather than natural selection.
   Evolutionary biologist Michael Lynch has argued that some of the
genomic changes that promote greater complexity of organisms, such as
regulatory changes that permit the advanced multicellularity of metazoa,
might have occurred not because they are adaptive but through random
genetic drift. Is there, after all, really such an obvious advantage to being
multicellular? If so, we don’t know what it is.
   Besides, if such a general advantage existed, we might reasonably expect
complex multicellular organisms to have arisen many times within the vast
unicellular world that still dominates the global biosphere. Yet, apparently,
they did not. Complex multicellularity has arisen only twice during
evolution: in animals and in plants. (Fungi might be deemed a third group,
but they don’t have anything like the tissue diversity of plants and
animals.)7 “Given the massive global dominance of unicellular species over
multicellular eukaryotes, both in terms of species richness and numbers of
individuals,” Lynch writes, “[then] if there is an advantage of organismal
complexity, one can only marvel at the inability of natural selection to
promote it.” What’s more, there are certainly some serious drawbacks to
being multicellular—as we’ll see in chapter 10.
    If Lynch is right, the implication is humbling: we are here not because
the multicellular lifestyle of metazoans like us is superior or even
advantageous (although clearly it is successful enough), but because chance
mutations created possibilities for new regulatory and multicellular
behaviors that natural selection merely found no reason to eliminate. The
work of Ruiz-Trillo on unicellular species is consistent with that idea:
innovations that enable multicellularity don’t by any means seem to demand
it. To put it another way, even with such options present, natural selection
alone might not be a sufficient force to “escape” from the single-celled
lifestyle. To do that requires, from an anthropocentric perspective, a further
dash of sheer luck.
    Evolution via new modes of gene regulation—shifting causation to
higher levels of organization—is a phenomenon that persisted as organisms
of ever greater complexity emerged. In 2011, developmental biologists
Craig Lowe and David Haussler and their colleagues looked at how the
mechanisms of gene regulation have evolved since the appearance of the
earliest vertebrates about 650 million years ago. The usual place to start for
understanding evolution in the age of the gene is with a comparison of
genomes between organisms, and indeed this is wonderfully informative.
By enumerating similarities and differences between genome sequences,
researchers can deduce how the various organisms diverged: in what order,
and therefore, to some degree, at what point in time. They can create so-
called molecular phylogenies: versions of the “tree of life” that can be
compared with those deduced from the older tradition of comparing
anatomies, thereby resolving some disputes about what evolved from what.
    The comparisons that Lowe and colleagues conducted were much more
specific than this. They considered fragments of genome sequences called
nonexonic elements, which are sequences that fall outside of the exons that
encode protein structures. They looked outside not only protein-coding
sequences but also outside of sequences known to encode regulatory RNAs
—that is, outside of what are now often called noncoding genes. Their
hypothesis was that if some of these nonexonic elements are found to be
highly conserved—to recur more or less unchanged in the genomes of
different species—we can assume they have some functional role and so are
subjected to selective pressure which preserves them: they aren’t just
random junk that would be expected quickly to degenerate and diverge
between different species. Such conserved nonexonic elements (CNEEs)
will probably have regulatory functions.
   The researchers already knew that many of the differences in shape and
function in the bodies of animals arise from differences in gene regulatory
elements rather than gains or losses of entirely new genes. They figured that
CNEEs might point to what kinds of regulatory changes have happened
over the evolutionary history of vertebrate animals. Lowe and colleagues
compared CNEEs in the genomes of humans, cows, mice, and two types of
fish (sticklebacks and Japanese medaka), looking for which of them these
organisms share in common (and thus which their common ancestors
presumably had too).
   They found that, rather than there being smooth and gradual changes in
the frequencies of CNEEs, three distinct eras of change seem to have
occurred over the past 650 million years. Until about 300 million years ago,
when mammals split from birds and reptiles, changes in regulation seem to
have happened mostly in parts of the genome close to transcription factors
and the key developmental genes that they control. Then between 300 and
100 million years ago those changes tailed off, and instead there were
changes near genes that code for the protein molecules serving as receptors
of signals at the cell surface. In other words, what seemed to matter for
these evolutionary changes was a shift in the way cells talk to one another.
Finally, since 100 million years ago, as placental mammals (that is, all
mammals except marsupials and monotremes like the echidnas) developed,
the regulatory changes seem to be associated with mechanisms for
modifying protein structure after translation, especially for proteins that are
associated with signal transduction within cells.
   Evolution, then, might be considered to have successively discovered
ways to innovate and generate new organisms by first reshuffling how
developmental genes are switched on and off, then how cells communicate,
and then how information gets passed around inside cells. In all cases the
action is taking place not at the genetic level but at higher levels of network
organization (which nevertheless leave traces in the genomes). This work
confirms the view expressed by Michel Morange that “the major changes
observed during evolution are more the consequence of the reorganization
of [gene regulatory] networks than the modification of the protein links that
form them.”

Casual Spreading
If these views are correct, what they imply is profound. The central pillar of
our understanding of life is that it is a unified phenomenon. This was
suspected centuries ago, but Darwin’s theory of evolution established how it
could be so, and the Modern Synthesis of the early twentieth century
deepened that understanding. At some levels the unity is undeniable. Aside
from the well-acknowledged complication of viruses, all life is cellular,
passes on hereditary information in DNA, and uses proteins and a relatively
small palette of other molecular types. This common ground gave rise to the
idea that we can understand a great deal about more complex organisms
such as ourselves by studying simpler ones, while recognizing that there
will be important differences in detail: what is true for E. coli was thought
to be true for the elephant.
   But the grandeur of Darwin’s vision has tended to inhibit a willingness to
see or accept that those differences might extend to more than mere details.
Indeed, some major distinctions between extant forms of life are well
accepted: we’ve seen that the way eukaryotic cells are organized is very
different from prokaryotes, and we will also see that the cells of
multicellular organisms have to satisfy very different demands than do
single-celled organisms. However, the general view is that there was no
shift in principles involved in these evolutionary transitions. DNA still
coded for proteins, proteins still catalyzed metabolic reactions, and all took
place within the insulated microenvironment of the cell.
   The work I’ve described in this chapter, however, seems to suggest that
what changed over the course of evolution is nothing less than the locus of
causation. I have called this causal spreading.8
   So if we want to understand the mechanisms behind some key
evolutionary shifts—for example, the emergence of complex body shapes
and lifestyles in the Cambrian explosion, the emergence of nervous systems
and of new modes of cognition, and the divergence of mammals and other
vertebrates—genomes are the wrong place to look. All we can hope to find
there are echoes of the true causal factors that happened at a higher level of
organization—in particular, changes within the networks of interaction
between and regulation of the molecular components, and changes in the
ways cells themselves interact, stick, and collectively transform one
another.
   I am convinced that the same story goes for the emergence of human-
level cognition. Much of our cognitive capacity is nothing special at all. We
don’t have the largest brains, for instance: adult sperm whale brains have a
volume more than three times greater.9 Many of our mental faculties, such
as the ability to navigate space or remember items, are equaled or exceeded
by other organisms. Every so often, researchers will claim to have identified
some crucial gene that allegedly underpins human-like cognition and
distinguishes us from other great apes; such claims have a habit of
evaporating as we discover more about the gene in question (see box 5.1). I
think we will find that what gave us cognitive abilities no other species
possesses—in particular, the ability to develop language, to think abstractly,
and to maintain highly nuanced social interactions—is a change at a higher
level than the genomic: a change in the emergent properties of the brain. No
single gene “made us human.”
   What makes this story so complicated—and has hindered us from seeing
it sooner—is that the migration of causation to higher systemic levels is not
total; hence “spreading,” not “shift.” As Hoel and colleagues showed (see
fig. 5.10), causal emergence is stronger for eukaryotes but does not wholly
replace lower-level causation. But even when individual genes retain some
causal power, it can be a slippery thing to assign, as we’ll see in chapter 10.
The change in conceptual framework demanded by causal spreading is thus
subtle.
   But it does need to change. Let me give you an example of how the old
notion of how life works—that is, by ever more elaboration of the same
basic principles—leads even experts astray. When I wrote some years ago
about the ENCODE project’s discovery of the ubiquity of transcriptional
activity throughout the genome, one expert on transcription and regulation
(he has, I’m sure, been nominated for a Nobel Prize for his seminal work on
the regulation of transcription in bacteria) wrote to me indignantly. If all
that RNA was truly functional, he asked, how could any specificity of
outcome arise when there is no specificity in the molecular interactions? He
added that François Jacob, the co-discoverer of the bacterial operon, who
had recently died, must be spinning in his grave!
   The question this fellow asked—how can specificity of effect arise
without specificity of interaction?—was excellent. But he was not
demanding an answer; he raised it rhetorically as an obvious absurdity. At
the time, I had no idea how to respond. Now I do. Such things are perfectly
possible via a relocation of the key causative processes to levels beyond
that of individual molecules and their interactions. Steeped in the regulatory
mechanisms of prokaryotes, this expert could not imagine such things.
   This is why I was so careful to point out at the outset that “how life
works” does not have a universal answer. To address the question for
humans, we will need to consider it at the human scale. Let’s now take the
first step beyond the molecular world and look at the causative mechanisms
of our cells.

 Box 5.1: What Makes Us Different?
 A rather striking illustration of how subtle regulatory changes can cause
 important evolutionary shifts was reported in 2021 by developmental
 biologist Madeline Lancaster and her colleagues. They investigated how
 human brains differ from those of other apes (gorillas and chimpanzees)
 by culturing neurons in a dish so that they developed into miniature
 brain-like structures called organoids (see p. 426). Our instinct might be
 to suppose that some gene mutation distinguishes our brains from those
 of other primates. But the researchers found that the differences in
 appearance of human and ape brain organoids seemed to result from a
 change in shape of the cells that are the precursors of neurons—that is,
 the changes appear before neurons as such begin to develop at all. This
 shape change appeared later in the growth of human brain organoids than
 in those of apes. Lancaster and colleagues traced the change to the way a
 particular gene called ZEB2 was expressed. The ZEB2 gene product is a
 transcription factor that regulates differentiation of the neuronal
 precursor cells. The crucial factor seemed to be not what this gene
expresses but when it is expressed: it happens earlier in the ape brain
organoids than in the human ones. When the researchers manipulated the
human organoids so that they expressed ZEB2 earlier, the organoids
looked more like those of a gorilla. This isn’t to suggest that all the
cognitive differences between humans and other great apes are created
by this difference in the timing of a change in cell shape. But it does
show that at least a part of the distinction may come from changes in the
precise dynamics—the timing—of gene regulation, and not in any
mutation of a key “cognition gene.”
   Here is why those popular tropes about us being 98.8 percent
genetically identical to chimpanzees, or for that matter 50 percent
identical to bananas, are trite to the point of being mistaken. You might
as well say that our chemical composition—how much of each element
we contain—is nearly identical. It’s true, but it connotes very little. It is
just not at the level of these ingredients that the action is happening. As
François Jacob observed decades ago, “what makes one vertebrate
different from another is a change in the time of expression and in the
relative amounts of gene products rather than the small differences
observed in the structure of these products. It is a matter of regulation
rather than structure.” What Jacob did not stress, but we now see, is that
for this very reason it is at the level of regulatory networks, and not at the
level of genes, that the causation here becomes focused.
