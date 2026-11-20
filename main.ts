import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// Copies POST.json from the repo root into the make.fun output dir.
// Stdlib only; nothing else.
const root = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "out";
mkdirSync(outDir, { recursive: true });
const post = readFileSync(join(root, "POST.json"), "utf8");
writeFileSync(join(outDir, "POST.json"), post);
