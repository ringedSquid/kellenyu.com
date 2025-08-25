# Zoom-Zoom-CPU
A simple 16-bit CPU with an integrated Keccakf1600 accelerator. My capstone project that I and a group of 4 other students worked on for the MIT Beaver Works Summer Institute program. Featured in Tiny Tapout 8. My main contribution to this project was putting together the assembler and verification.
<br>

### [github repo](https://github.com/ringedSquid/BWSI-ASICS-24-Zoom-Zoom/tree/main) [TT08](https://tinytapeout.com/chips/tt08/tt_um_zoom_zoom)
<br>

## High level overview
<img src="./Zoom-Zoom-CPU/media/blockdiagram.png" alt="blockdiagram.png" width="75%">
<br>

## Detailed List of Features
- Custom Architecture and ISA
  - 16-bit instructions
  - 5 types of instructions
- 6 general purpose registers
  - 1 flag register
  - 1 zero register
- UART Interface
- SPI and Custom Parallel Memeroy Interface
  - 16 bit memory address
  - supports up to 65536 memory addresses(2^16)
- Flexible design easy integration of accelerators as instructions
<br>

## The Architecture

<img src="./Zoom-Zoom-CPU/media/architecture.png" alt="architecture" width="75%">
<br>

### Instruction Layout & Registers

<img src="./Zoom-Zoom-CPU/media/Registers.png" alt="Registers" width="75%">
<br>

### General Instructions

<img src="./Zoom-Zoom-CPU/media/Instructions.png" alt="Instructions" width="75%">
<br>

## Programming the CPU

**Memory Address 769 is reserved**: The Assembler does not give a warning currently!
<br>

To assemble, use [custoasm](https://github.com/hlorenzi/customasm) with installation instructions [here](https://github.com/hlorenzi/customasm?tab=readme-ov-file#installation). We recommend installation via rust's package manager by running ```cargo install customasm```. You can then compile an assembly file by running ```customasm -o <outputfilename> <filename>```. The format for the assembly file is to add ```#include "x3q16_ruleset.asm"``` to the top of each .asm file as well as that file which is located [here](../asm/x3q16_ruleset.asm). Instruction memory and General Purpose are all located in the same place. Thus, to store general values in memory, just jump to wherever you store it in memory.
<br>

## Accelerators

**Many are still a work in progress or aren't supported by the assembler**
<br>

### Keccakf1600

Approximately 50% of the computational time for the Kyber Algorithm is hashing needed for random number generation. The Kyber algorthm uses SHA-3 and SHAKE algorithms to generate cryptographically secure random polynomials and numbers. Both of these algorithm rely on the keccakf1600 state permutation which target to accelerate. More information on the keccak algorithm can be found [here](https://keccak.team/keccak_specs_summary.html) and the kyber algorithm [here](https://pq-crystals.org/kyber/data/kyber-specification-round3-20210804.pdf).

The branch ```keccak_integration``` holds a complete state permuation accelerator however this is not included in main since it's too big to fit for tinytapeout. A smaller accelerator is currently being worked on.
<br>

## How to test

Generate the binary file from test/x3q16 and load it into memory. Reset the chip and see if anything is written in memory.
<br>

## External hardware

Either a SPI ram chip or a MCU emulator of parallel storage with custom protocol