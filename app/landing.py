from html import escape

LANDING_TEMPLATE = """<!doctype html>

<html class="dark scroll-smooth" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <title>
      GeoMeasure API — Geospatial File Measurement &amp; Spatial Pipeline
    </title>
    <link href="https://fonts.googleapis.com" rel="preconnect" />
    <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect" />
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;display=swap"
      rel="stylesheet"
    />
    <link
      href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap"
      rel="stylesheet"
    />
    <link
      href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap"
      rel="stylesheet"
    />
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            colors: {
              "inverse-on-surface": "#2a3040",
              "error-container": "#93000a",
              "on-secondary-fixed": "#002114",
              secondary: "#45dfa4",
              "on-tertiary-fixed-variant": "#643f00",
              "on-surface-variant": "#bbc9cd",
              "on-surface": "#dde2f8",
              "on-secondary-container": "#00452e",
              "on-secondary-fixed-variant": "#005137",
              outline: "#859397",
              "on-secondary": "#003825",
              "surface-container-low": "#151b2b",
              "surface-variant": "#2f3445",
              "tertiary-fixed": "#ffddb5",
              "on-tertiary-container": "#6e4600",
              primary: "#8aebff",
              "tertiary-fixed-dim": "#ffb957",
              "primary-fixed": "#a2eeff",
              "on-tertiary": "#462b00",
              "inverse-primary": "#006877",
              "surface-dim": "#0d1322",
              "surface-container-lowest": "#080e1d",
              "secondary-container": "#00bd85",
              background: "#0d1322",
              "on-primary-fixed-variant": "#004e5a",
              "primary-fixed-dim": "#2fd9f4",
              "surface-bright": "#33394a",
              "inverse-surface": "#dde2f8",
              "surface-container-high": "#242a3a",
              error: "#ffb4ab",
              "on-error-container": "#ffdad6",
              "on-primary-container": "#005763",
              "outline-variant": "#3c494c",
              "surface-tint": "#2fd9f4",
              "secondary-fixed": "#68fcbf",
              "on-background": "#dde2f8",
              "surface-container-highest": "#2f3445",
              "primary-container": "#22d3ee",
              "tertiary-container": "#ffb13b",
              "surface-container": "#191f2f",
              surface: "#0d1322",
              "on-error": "#690005",
              "on-primary-fixed": "#001f25",
              "on-primary": "#00363e",
              "on-tertiary-fixed": "#2a1800",
              "secondary-fixed-dim": "#45dfa4",
              tertiary: "#ffd6a3",
            },
            borderRadius: {
              DEFAULT: "0.125rem",
              lg: "0.25rem",
              xl: "0.5rem",
              full: "0.75rem",
            },
            spacing: {
              gutter: "1rem",
              "space-sm": "0.5rem",
              "space-md": "1rem",
              "space-xs": "0.25rem",
              margin: "1rem",
              "space-2xl": "3rem",
              "space-lg": "1.5rem",
              "space-xl": "2rem",
              "space-xxs": "0.125rem",
              "gutter-desktop": "1.5rem",
              "margin-desktop": "3rem",
              "space-3xl": "4rem",
              "margin-tablet": "2rem",
            },
            fontFamily: {
              "headline-md": ["Inter"],
              "headline-sm": ["Inter"],
              "body-sm": ["Inter"],
              "label-sm": ["Inter"],
              "code-md": ["monospace"],
              "headline-lg-mobile": ["Inter"],
              "label-md": ["Inter"],
              "body-md": ["Inter"],
              "display-hero-mobile": ["Inter"],
              "body-lg": ["Inter"],
              "display-hero": ["Inter"],
              "headline-lg": ["Inter"],
              "code-sm": ["monospace"],
            },
            fontSize: {
              "headline-md": [
                "20px",
                {
                  lineHeight: "28px",
                  letterSpacing: "-0.015em",
                  fontWeight: "600",
                },
              ],
              "headline-sm": [
                "16px",
                {
                  lineHeight: "24px",
                  letterSpacing: "-0.01em",
                  fontWeight: "600",
                },
              ],
              "body-sm": [
                "12px",
                { lineHeight: "18px", letterSpacing: "0em", fontWeight: "400" },
              ],
              "label-sm": [
                "11px",
                {
                  lineHeight: "14px",
                  letterSpacing: "0.04em",
                  fontWeight: "500",
                },
              ],
              "code-md": [
                "13px",
                { lineHeight: "20px", letterSpacing: "0em", fontWeight: "400" },
              ],
              "headline-lg-mobile": [
                "24px",
                {
                  lineHeight: "32px",
                  letterSpacing: "-0.02em",
                  fontWeight: "600",
                },
              ],
              "label-md": [
                "13px",
                {
                  lineHeight: "16px",
                  letterSpacing: "0.01em",
                  fontWeight: "500",
                },
              ],
              "body-md": [
                "14px",
                { lineHeight: "22px", letterSpacing: "0em", fontWeight: "400" },
              ],
              "display-hero-mobile": [
                "32px",
                {
                  lineHeight: "40px",
                  letterSpacing: "-0.02em",
                  fontWeight: "600",
                },
              ],
              "body-lg": [
                "16px",
                {
                  lineHeight: "26px",
                  letterSpacing: "-0.005em",
                  fontWeight: "400",
                },
              ],
              "display-hero": [
                "48px",
                {
                  lineHeight: "56px",
                  letterSpacing: "-0.03em",
                  fontWeight: "600",
                },
              ],
              "headline-lg": [
                "30px",
                {
                  lineHeight: "38px",
                  letterSpacing: "-0.025em",
                  fontWeight: "600",
                },
              ],
              "code-sm": [
                "11px",
                {
                  lineHeight: "16px",
                  letterSpacing: "0.02em",
                  fontWeight: "500",
                },
              ],
            },
          },
        },
      };
    </script>
    <style>
      .material-symbols-outlined {
        font-variation-settings:
          "FILL" 0,
          "wght" 400,
          "GRAD" 0,
          "opsz" 20;
        font-size: 1.15rem;
        vertical-align: middle;
        display: inline-block;
        line-height: 1;
      }
      .grid-lines-bg {
        background-size: 32px 32px;
        background-image:
          linear-gradient(
            to right,
            rgba(60, 73, 76, 0.18) 1px,
            transparent 1px
          ),
          linear-gradient(
            to bottom,
            rgba(60, 73, 76, 0.18) 1px,
            transparent 1px
          );
      }
      .hud-glow {
        box-shadow:
          0 0 0 1px #22d3ee,
          0 0 16px rgba(34, 211, 238, 0.25);
      }
    </style>
  </head>
  <body
    class="bg-background text-on-surface antialiased selection:bg-primary-container selection:text-surface-dim min-h-screen flex flex-col font-body-md text-body-md relative overflow-x-hidden"
  >
    <div class="fixed inset-0 pointer-events-none z-0 overflow-hidden">
      <div
        class="absolute -top-32 left-1/4 w-96 h-96 bg-primary-container/10 rounded-full blur-3xl"
      ></div>
      <div
        class="absolute top-1/2 -right-32 w-96 h-96 bg-secondary/5 rounded-full blur-3xl"
      ></div>
      <div class="absolute inset-0 grid-lines-bg opacity-70"></div>
    </div>
    <!-- NavBar -->
    <header
      class="fixed top-0 left-0 w-full z-50 flex items-center justify-between px-margin md:px-margin-tablet lg:px-margin-desktop h-14 bg-surface-dim/95 dark:bg-surface-dim/95 backdrop-blur-md border-b border-outline-variant dark:border-outline-variant"
    >
      <div class="flex items-center gap-space-lg">
        <a
          class="text-headline-sm font-headline-sm font-semibold tracking-tight text-on-surface dark:text-on-surface flex items-center gap-space-xs group"
          href="#"
        >
          <div
            class="w-7 h-7 rounded-lg bg-surface-container-high border border-outline-variant flex items-center justify-center text-primary-container group-hover:border-primary-container transition-colors"
          >
            <span class="material-symbols-outlined" data-icon="polyline"
              >polyline</span
            >
          </div>
          <span>GeoMeasure API</span>
          <span
            class="font-code-sm text-code-sm px-1.5 py-0.5 rounded bg-surface-container-high border border-outline-variant text-primary-fixed"
            >v1.4</span
          >
        </a>
       
        <nav
          class="hidden md:flex items-center gap-space-md ml-space-sm font-label-md text-label-md"
        >
          <a
            class="text-primary dark:text-primary border-b-2 border-primary dark:border-primary pb-1"
            href="#endpoints"
            >Endpoints</a
          >
          <a
            class="text-on-surface-variant dark:text-on-surface-variant transition-colors duration-150 hover:text-primary dark:hover:text-primary"
            href="#schema"
            >Coordinate Reference</a
          >
          <a
            class="text-on-surface-variant dark:text-on-surface-variant transition-colors duration-150 hover:text-primary dark:hover:text-primary"
            href="#response"
            >GeoJSON Specs</a
          >
          <a
            class="text-on-surface-variant dark:text-on-surface-variant transition-colors duration-150 hover:text-primary dark:hover:text-primary"
            href="#capabilities"
            >Changelog</a
          >
        </nav>
      </div>
      <!-- Trailing Action Cluster -->
      <div class="flex items-center gap-space-md">
        <!-- Live Telemetry Status indicator -->
        <div
          class="hidden sm:flex items-center gap-2 px-2.5 py-1 rounded bg-surface-container-lowest border border-outline-variant font-code-sm text-code-sm text-on-surface-variant"
        >
          <span class="relative flex h-2 w-2">
            <span
              class="animate-ping absolute inline-flex h-full w-full rounded-full bg-secondary opacity-75"
            ></span>
            <span
              class="relative inline-flex rounded-full h-2 w-2 bg-secondary"
            ></span>
          </span>
          <span>Status: 99.98%</span>
        </div>
        <div class="flex items-center gap-space-xs text-on-surface-variant">
          <a
            class="p-1.5 rounded hover:bg-surface-variant hover:text-primary transition-colors"
            href="/docs"
            rel="noreferrer"
            target="_blank"
            title="Terminal Interface"
          >
            <span class="material-symbols-outlined" data-icon="terminal"
              >terminal</span
            >
          </a>
          <a
            class="p-1.5 rounded hover:bg-surface-variant hover:text-primary transition-colors"
            href="/openapi.json"
            rel="noreferrer"
            target="_blank"
            title="API Schema Code"
          >
            <span class="material-symbols-outlined" data-icon="code">code</span>
          </a>
        </div>
        <a
          class="bg-primary-container hover:bg-primary-fixed-dim text-surface-dim font-headline-sm text-label-md px-3.5 py-1.5 rounded-lg flex items-center gap-1.5 transition-all scale-[0.99] duration-100 ease-out shadow-sm font-semibold"
          href="#documentation"
        >
          <span>API Documentation</span>
          <span
            class="material-symbols-outlined text-sm"
            data-icon="arrow_forward"
            >arrow_forward</span
          >
        </a>
      </div>
    </header>
    
    <main class="flex-1 z-10 pt-20">
      <section
        class="px-margin md:px-margin-tablet lg:px-margin-desktop py-space-xl lg:py-space-3xl max-w-7xl mx-auto"
      >
        <div
          class="grid grid-cols-1 lg:grid-cols-12 gap-space-xl lg:gap-gutter-desktop items-center"
        >
          <div class="lg:col-span-7 flex flex-col items-start space-y-space-md">
            <div
              class="inline-flex items-center gap-2 px-3 py-1 rounded bg-surface-container-high border border-outline-variant text-primary-fixed font-code-sm text-code-sm tracking-wider"
            >
              <span
                class="w-1.5 h-1.5 rounded-full bg-primary-container animate-pulse"
              ></span>
              <span>DEVELOPER-FIRST GEOSPATIAL PROCESSING</span>
            </div>
            <h1
              class="hidden lg:block font-display-hero text-display-hero text-on-surface tracking-tight leading-tight"
            >
              Measure the World.<br />
              <span
                class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-primary-container"
                >Build with Coordinates.</span
              >
            </h1>
            <h1
              class="lg:hidden font-display-hero-mobile text-display-hero-mobile text-on-surface tracking-tight"
            >
              Measure the World.<br />
              <span
                class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-primary-container"
                >Build with Coordinates.</span
              >
            </h1>
            <p
              class="font-body-lg text-body-lg text-on-surface-variant max-w-xl"
            >
              A powerful API interface for geospatial file measurement and
              spatial data processing. Explore endpoints, understand the API
              schema, and integrate geospatial capabilities into your
              applications.
            </p>
            <div class="flex flex-wrap items-center gap-space-sm pt-space-xs">
              <a
                class="bg-primary-container hover:bg-primary-fixed-dim text-surface-dim font-headline-sm text-label-md px-5 py-2.5 rounded-lg flex items-center gap-2 transition-all"
                href="#documentation"
              >
                <span>Explore API Docs</span>
                <span
                  class="material-symbols-outlined"
                  data-icon="arrow_forward"
                  >arrow_forward</span
                >
              </a>
              <a
                class="bg-surface-container-high hover:border-primary border border-outline-variant text-on-surface hover:text-primary font-headline-sm text-label-md px-5 py-2.5 rounded-lg flex items-center gap-2 transition-all"
                href="/openapi.json"
                rel="noreferrer"
                target="_blank"
              >
                <span>View OpenAPI Schema</span>
                <span class="material-symbols-outlined" data-icon="open_in_new"
                  >open_in_new</span
                >
              </a>
            </div>
            <div
              class="pt-space-xs flex items-center gap-4 text-outline font-code-sm text-code-sm"
            >
              <span class="flex items-center gap-1.5">
                <span
                  class="material-symbols-outlined text-primary-container"
                  data-icon="check_circle"
                  >check_circle</span
                >
                REST API
              </span>
              <span class="text-outline-variant">/</span>
              <span class="flex items-center gap-1.5">
                <span
                  class="material-symbols-outlined text-primary-container"
                  data-icon="check_circle"
                  >check_circle</span
                >
                OpenAPI 3.1
              </span>
              <span class="text-outline-variant">/</span>
              <span class="flex items-center gap-1.5">
                <span
                  class="material-symbols-outlined text-secondary"
                  data-icon="bolt"
                  >bolt</span
                >
                Developer Ready
              </span>
            </div>
          </div>
          <div class="lg:col-span-5 relative">
            <div
              class="relative bg-surface-container-lowest border border-outline-variant rounded-xl p-4 overflow-hidden shadow-2xl"
            >
              <div class="absolute inset-0 grid-lines-bg opacity-30"></div>
              <div
                class="absolute top-2 left-3 font-code-sm text-code-sm text-outline flex items-center gap-2"
              >
                <span
                  class="w-1.5 h-1.5 bg-primary-container rounded-full"
                ></span>
                <span>CANVAS : 51.5074° N, 0.1278° W</span>
              </div>
              <div
                class="absolute top-2 right-3 font-code-sm text-code-sm text-outline"
              >
                EPSG:4326
              </div>
              <div
                class="relative w-full h-80 rounded-lg bg-surface-container-low/70 border border-outline-variant flex items-center justify-center overflow-hidden my-4"
              >
                <svg
                  class="absolute inset-0 w-full h-full opacity-20 stroke-primary"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M-20 60 Q 80 120 180 40 T 380 90 T 500 40"
                    stroke-width="1"
                  ></path>
                  <path
                    d="M-20 120 Q 120 180 240 80 T 420 140 T 520 100"
                    stroke-dasharray="2 3"
                    stroke-width="1"
                  ></path>
                  <path
                    d="M-20 200 Q 100 240 260 180 T 440 220 T 520 180"
                    stroke-width="1"
                  ></path>
                  <path
                    d="M-20 260 Q 140 290 280 230 T 460 270 T 520 240"
                    stroke-dasharray="4 2"
                    stroke-width="1"
                  ></path>
                </svg>
                <div
                  class="absolute inset-0 flex items-center justify-center pointer-events-none"
                >
                  <div class="w-full h-[1px] bg-outline-variant/50"></div>
                  <div
                    class="h-full w-[1px] bg-outline-variant/50 absolute"
                  ></div>
                  <div
                    class="w-48 h-48 rounded-full border border-outline-variant/40 animate-pulse"
                  ></div>
                  <div
                    class="w-64 h-64 rounded-full border border-primary-container/20"
                  ></div>
                </div>
                <svg
                  class="relative z-10 w-72 h-56"
                  fill="none"
                  viewbox="0 0 280 200"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <polygon
                    fill="rgba(34, 211, 238, 0.12)"
                    points="50,45 220,35 245,155 120,175 40,115"
                    stroke="#22D3EE"
                    stroke-linejoin="round"
                    stroke-width="1.75"
                  ></polygon>
                  <circle
                    cx="50"
                    cy="45"
                    fill="#080E1D"
                    r="4"
                    stroke="#22D3EE"
                    stroke-width="2"
                  ></circle>
                  <circle
                    cx="220"
                    cy="35"
                    fill="#080E1D"
                    r="4"
                    stroke="#22D3EE"
                    stroke-width="2"
                  ></circle>
                  <circle
                    cx="245"
                    cy="155"
                    fill="#080E1D"
                    r="4"
                    stroke="#22D3EE"
                    stroke-width="2"
                  ></circle>
                  <circle
                    cx="120"
                    cy="175"
                    fill="#080E1D"
                    r="4"
                    stroke="#22D3EE"
                    stroke-width="2"
                  ></circle>
                  <circle
                    cx="40"
                    cy="115"
                    fill="#080E1D"
                    r="4"
                    stroke="#22D3EE"
                    stroke-width="2"
                  ></circle>
                  <circle cx="135" cy="105" fill="#34D399" r="2.5"></circle>
                </svg>
                <div
                  class="absolute bottom-3 left-3 bg-surface-container-high/90 backdrop-blur border border-outline-variant rounded p-2 text-left z-20"
                >
                  <div
                    class="flex items-center justify-between gap-3 font-code-sm text-code-sm text-primary"
                  >
                    <span>VERTEX_01</span>
                    <span class="w-1.5 h-1.5 rounded-full bg-secondary"></span>
                  </div>
                  <div
                    class="font-code-sm text-code-sm text-on-surface-variant mt-0.5"
                  >
                    LAT: 51.5074° · LNG: -0.1278°
                  </div>
                </div>
                <div
                  class="absolute top-8 right-3 bg-surface-container-high/90 backdrop-blur border border-outline-variant rounded p-2 text-left z-20"
                >
                  <div class="font-code-sm text-code-sm text-outline">
                    GEODESIC_AREA
                  </div>
                  <div
                    class="font-code-md text-code-md text-on-surface font-semibold flex items-baseline gap-1"
                  >
                    <span>4.821</span>
                    <span
                      class="font-code-sm text-code-sm text-primary-container"
                      >km²</span
                    >
                  </div>
                  <div class="font-code-sm text-code-sm text-outline mt-0.5">
                    PERIMETER: 9.14 km
                  </div>
                </div>
              </div>
              <div
                class="bg-surface-container-low border border-outline-variant rounded p-2.5 font-code-sm text-code-sm text-on-surface-variant flex items-center justify-between"
              >
                <div class="flex items-center gap-2">
                  <span class="text-secondary font-bold">POST</span>
                  <span class="text-on-surface">/v1/measure/geodesic</span>
                </div>
                <div class="flex items-center gap-1.5 text-primary">
                  <span
                    class="w-2 h-2 rounded-full bg-secondary inline-block"
                  ></span>
                  <span>200 OK · 18ms</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section
        class="px-margin md:px-margin-tablet lg:px-margin-desktop py-space-2xl max-w-7xl mx-auto border-t border-outline-variant/60"
        id="documentation"
      >
        <div class="max-w-2xl mb-space-xl">
          <div
            class="font-code-sm text-code-sm text-primary-container tracking-wider uppercase mb-1 flex items-center gap-2"
          >
            <span
              class="material-symbols-outlined text-sm"
              data-icon="integration_instructions"
              >integration_instructions</span
            >
            <span>EXPLORATION &amp; SCHEMA SPECIFICATION</span>
          </div>
          <h2
            class="font-headline-lg text-headline-lg text-on-surface tracking-tight"
          >
            Everything You Need to Integrate
          </h2>
          <p class="font-body-md text-body-md text-on-surface-variant mt-2">
            Choose your preferred way to explore the API, inspect its schema,
            and test available endpoints with instant visual feedback.
          </p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-space-lg">
          <div
            class="group bg-surface-container-low hover:bg-surface-container border border-outline-variant hover:border-primary-container transition-all duration-200 rounded-lg p-space-lg flex flex-col justify-between relative hover:hud-glow"
          >
            <div>
              <div class="flex items-center justify-between mb-space-md">
                <div
                  class="w-10 h-10 rounded bg-surface-container-high border border-outline-variant flex items-center justify-center text-primary group-hover:text-primary-container transition-colors"
                >
                  <span class="material-symbols-outlined" data-icon="terminal"
                    >terminal</span
                  >
                </div>
                <span
                  class="font-code-sm text-code-sm px-2 py-0.5 rounded bg-primary-container/10 border border-primary-container/30 text-primary-container"
                >
                  SWAGGER UI
                </span>
              </div>
              <h3
                class="font-headline-md text-headline-md text-on-surface mb-2"
              >
                Interactive Docs
              </h3>
              <p
                class="font-body-sm text-body-sm text-on-surface-variant mb-space-lg"
              >
                Explore API endpoints, inspect request and response schemas, and
                test supported operations through the interactive Swagger
                interface.
              </p>
            </div>
            <div class="pt-4 border-t border-outline-variant/40">
              <a
                class="w-full inline-flex items-center justify-between font-label-md text-label-md text-primary group-hover:text-primary-fixed-dim transition-colors"
                href="/docs"
                rel="noreferrer"
                target="_blank"
              >
                <span>Open Swagger Docs</span>
                <span
                  class="material-symbols-outlined text-sm"
                  data-icon="arrow_outward"
                  >arrow_outward</span
                >
              </a>
            </div>
          </div>
          <!-- Card 2: ReDoc Reference -->
          <div
            class="group bg-surface-container-low hover:bg-surface-container border border-outline-variant hover:border-primary-container transition-all duration-200 rounded-lg p-space-lg flex flex-col justify-between relative hover:hud-glow"
          >
            <div>
              <div class="flex items-center justify-between mb-space-md">
                <div
                  class="w-10 h-10 rounded bg-surface-container-high border border-outline-variant flex items-center justify-center text-primary group-hover:text-primary-container transition-colors"
                >
                  <span class="material-symbols-outlined" data-icon="menu_book"
                    >menu_book</span
                  >
                </div>
                <span
                  class="font-code-sm text-code-sm px-2 py-0.5 rounded bg-secondary/10 border border-secondary/30 text-secondary"
                >
                  REDOC
                </span>
              </div>
              <h3
                class="font-headline-md text-headline-md text-on-surface mb-2"
              >
                API Reference
              </h3>
              <p
                class="font-body-sm text-body-sm text-on-surface-variant mb-space-lg"
              >
                Browse a clean, structured API reference with detailed endpoint
                descriptions, parameters, schemas, and response formats.
              </p>
            </div>
            <div class="pt-4 border-t border-outline-variant/40">
              <a
                class="w-full inline-flex items-center justify-between font-label-md text-label-md text-primary group-hover:text-primary-fixed-dim transition-colors"
                href="/redoc"
                rel="noreferrer"
                target="_blank"
              >
                <span>Read API Reference</span>
                <span
                  class="material-symbols-outlined text-sm"
                  data-icon="arrow_outward"
                  >arrow_outward</span
                >
              </a>
            </div>
          </div>
          <div
            class="group bg-surface-container-low hover:bg-surface-container border border-outline-variant hover:border-primary-container transition-all duration-200 rounded-lg p-space-lg flex flex-col justify-between relative hover:hud-glow"
          >
            <div>
              <div class="flex items-center justify-between mb-space-md">
                <div
                  class="w-10 h-10 rounded bg-surface-container-high border border-outline-variant flex items-center justify-center text-primary group-hover:text-primary-container transition-colors"
                >
                  <span
                    class="material-symbols-outlined"
                    data-icon="data_object"
                    >data_object</span
                  >
                </div>
                <span
                  class="font-code-sm text-code-sm px-2 py-0.5 rounded bg-surface-container-highest border border-outline-variant text-on-surface"
                >
                  JSON
                </span>
              </div>
              <h3
                class="font-headline-md text-headline-md text-on-surface mb-2"
              >
                OpenAPI Schema
              </h3>
              <p
                class="font-body-sm text-body-sm text-on-surface-variant mb-space-lg"
              >
                Access the machine-readable OpenAPI specification for API
                integrations, client generation, and automated tooling.
              </p>
            </div>
            <div class="pt-4 border-t border-outline-variant/40">
              <a
                class="w-full inline-flex items-center justify-between font-label-md text-label-md text-primary group-hover:text-primary-fixed-dim transition-colors"
                href="/openapi.json"
                rel="noreferrer"
                target="_blank"
              >
                <span>View JSON Schema</span>
                <span
                  class="material-symbols-outlined text-sm"
                  data-icon="arrow_outward"
                  >arrow_outward</span
                >
              </a>
            </div>
          </div>
        </div>
      </section>
      <section
        class="px-margin md:px-margin-tablet lg:px-margin-desktop py-space-2xl max-w-7xl mx-auto border-t border-outline-variant/60"
        id="capabilities"
      >
        <div class="max-w-2xl mb-space-xl">
          <div
            class="font-code-sm text-code-sm text-primary-container tracking-wider uppercase mb-1 flex items-center gap-2"
          >
            <span class="material-symbols-outlined text-sm" data-icon="token"
              >token</span
            >
            <span>HIGH-THROUGHPUT ENGINE</span>
          </div>
          <h2
            class="font-headline-lg text-headline-lg text-on-surface tracking-tight"
          >
            Built for Geospatial Workflows
          </h2>
          <p class="font-body-md text-body-md text-on-surface-variant mt-2">
            Engineered to calculate areas, lengths, coordinate envelopes, and
            vector geometries with millisecond latency.
          </p>
        </div>
        <div
          class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-space-md"
        >
          <div
            class="bg-surface-container-low border border-outline-variant rounded-lg p-space-md hover:border-outline transition-colors"
          >
            <div
              class="w-8 h-8 rounded bg-surface-container-high border border-outline-variant flex items-center justify-center text-primary-container mb-3"
            >
              <span class="material-symbols-outlined" data-icon="folder_zip"
                >folder_zip</span
              >
            </div>
            <div class="font-code-sm text-code-sm text-outline mb-1">
              MODULE_01
            </div>
            <h4 class="font-headline-sm text-headline-sm text-on-surface mb-1">
              Geospatial File Processing
            </h4>
            <p class="font-body-sm text-body-sm text-on-surface-variant">
              Designed for high-concurrency workflows involving geographic data
              files, Shapefiles, and GeoJSON streams.
            </p>
          </div>
          <div
            class="bg-surface-container-low border border-outline-variant rounded-lg p-space-md hover:border-outline transition-colors"
          >
            <div
              class="w-8 h-8 rounded bg-surface-container-high border border-outline-variant flex items-center justify-center text-primary-container mb-3"
            >
              <span class="material-symbols-outlined" data-icon="square_foot"
                >square_foot</span
              >
            </div>
            <div class="font-code-sm text-code-sm text-outline mb-1">
              MODULE_02
            </div>
            <h4 class="font-headline-sm text-headline-sm text-on-surface mb-1">
              Spatial Measurements
            </h4>
            <p class="font-body-sm text-body-sm text-on-surface-variant">
              A dedicated interface for exploring available geodesic distance,
              area computations, and vertex audits.
            </p>
          </div>
          <div
            class="bg-surface-container-low border border-outline-variant rounded-lg p-space-md hover:border-outline transition-colors"
          >
            <div
              class="w-8 h-8 rounded bg-surface-container-high border border-outline-variant flex items-center justify-center text-primary-container mb-3"
            >
              <span class="material-symbols-outlined" data-icon="schema"
                >schema</span
              >
            </div>
            <div class="font-code-sm text-code-sm text-outline mb-1">
              MODULE_03
            </div>
            <h4 class="font-headline-sm text-headline-sm text-on-surface mb-1">
              Structured API Responses
            </h4>
            <p class="font-body-sm text-body-sm text-on-surface-variant">
              Consistent, strictly documented request and response schemas
              adhering to RFC 7946 specifications.
            </p>
          </div>
          <div
            class="bg-surface-container-low border border-outline-variant rounded-lg p-space-md hover:border-outline transition-colors"
          >
            <div
              class="w-8 h-8 rounded bg-surface-container-high border border-outline-variant flex items-center justify-center text-primary-container mb-3"
            >
              <span class="material-symbols-outlined" data-icon="api">api</span>
            </div>
            <div class="font-code-sm text-code-sm text-outline mb-1">
              MODULE_04
            </div>
            <h4 class="font-headline-sm text-headline-sm text-on-surface mb-1">
              Developer Integration
            </h4>
            <p class="font-body-sm text-body-sm text-on-surface-variant">
              An OpenAPI-based interface that supports API exploration, typed
              client generation, and CI validation.
            </p>
          </div>
        </div>
      </section>
      <section
        class="px-margin md:px-margin-tablet lg:px-margin-desktop py-space-2xl max-w-7xl mx-auto border-t border-outline-variant/60"
        id="response"
      >
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-space-xl items-start">
          <div class="lg:col-span-5">
            <div
              class="font-code-sm text-code-sm text-primary-container tracking-wider uppercase mb-1 flex items-center gap-2"
            >
              <span
                class="material-symbols-outlined text-sm"
                data-icon="terminal"
                >terminal</span
              >
              <span>STANDARDIZED PAYLOAD</span>
            </div>
            <h2
              class="font-headline-lg text-headline-lg text-on-surface tracking-tight"
            >
              Understand the Data. Integrate with Confidence.
            </h2>
            <p class="font-body-md text-body-md text-on-surface-variant mt-3">
              GeoMeasure standardizes input files into unified, validated
              coordinate collections. All calculations preserve original
              precision with geodesic ellipsoidal calculations.
            </p>
            <div
              class="mt-6 space-y-3 font-code-sm text-code-sm text-on-surface-variant"
            >
              <div class="flex items-center gap-2">
                <span
                  class="material-symbols-outlined text-secondary text-sm"
                  data-icon="check"
                  >check</span
                >
                <span
                  >WGS84 (EPSG:4326) and Web Mercator (EPSG:3857) support</span
                >
              </div>
              <div class="flex items-center gap-2">
                <span
                  class="material-symbols-outlined text-secondary text-sm"
                  data-icon="check"
                  >check</span
                >
                <span>Deterministic floating-point rounding precision</span>
              </div>
              <div class="flex items-center gap-2">
                <span
                  class="material-symbols-outlined text-secondary text-sm"
                  data-icon="check"
                  >check</span
                >
                <span
                  >Fully compliant RFC 7946 GeoJSON topology serialization</span
                >
              </div>
            </div>
          </div>
          <div class="lg:col-span-7">
            <div
              class="rounded-lg bg-surface-container-lowest border border-outline-variant overflow-hidden shadow-2xl"
            >
              <!-- IDE Header Bar -->
              <div
                class="px-4 py-2.5 bg-surface-container border-b border-outline-variant flex items-center justify-between"
              >
                <div class="flex items-center gap-2">
                  <div class="flex items-center gap-1.5 mr-2">
                    <div
                      class="w-2.5 h-2.5 rounded-full bg-outline-variant"
                    ></div>
                    <div
                      class="w-2.5 h-2.5 rounded-full bg-outline-variant"
                    ></div>
                    <div
                      class="w-2.5 h-2.5 rounded-full bg-outline-variant"
                    ></div>
                  </div>
                  <div
                    class="px-2.5 py-1 bg-surface-container-lowest border-t-2 border-primary-container text-on-surface font-code-sm text-code-sm rounded-t flex items-center gap-1.5"
                  >
                    <span
                      class="material-symbols-outlined text-sm text-primary"
                      data-icon="code"
                      >code</span
                    >
                    <span>feature_response.geojson</span>
                  </div>
                </div>
                <button
                  class="flex items-center gap-1.5 px-2.5 py-1 rounded bg-surface-container-high hover:bg-surface-bright text-on-surface-variant hover:text-on-surface font-code-sm text-code-sm transition-all border border-outline-variant"
                  id="copy-btn"
                >
                  <span
                    class="material-symbols-outlined text-sm"
                    data-icon="content_copy"
                    id="copy-icon"
                    >content_copy</span
                  >
                  <span id="copy-text">Copy GeoJSON</span>
                </button>
              </div>
              <!-- Syntax Highlighted Code Viewer -->
              <pre
                class="p-space-lg font-code-md text-code-md overflow-x-auto text-on-surface bg-surface-container-lowest selection:bg-surface-variant"
              ><code id="code-snippet">{
  <span class="text-primary-container">"type"</span>: <span class="text-secondary">"Feature"</span>,
  <span class="text-primary-container">"geometry"</span>: {
    <span class="text-primary-container">"type"</span>: <span class="text-secondary">"Polygon"</span>,
    <span class="text-primary-container">"coordinates"</span>: [
      [
        [-0.12, 51.50],
        [-0.10, 51.50],
        [-0.10, 51.52],
        [-0.12, 51.52],
        [-0.12, 51.50]
      ]
    ]
  },
  <span class="text-primary-container">"properties"</span>: {
    <span class="text-primary-container">"measurement_unit"</span>: <span class="text-secondary">"meters"</span>
  }
}</code></pre>
              <div
                class="px-4 py-1.5 bg-surface-container-low border-t border-outline-variant flex items-center justify-between text-outline font-code-sm text-code-sm"
              >
                <span>GeoJSON RFC 7946 · UTF-8</span>
                <span class="text-secondary flex items-center gap-1">
                  <span class="w-1.5 h-1.5 rounded-full bg-secondary"></span>
                  Valid Geometry
                </span>
              </div>
            </div>
            <p class="font-body-sm text-body-sm text-outline mt-2.5 italic">
              Illustrative GeoJSON example — actual API request and response
              formats depend on the implemented endpoints.
            </p>
          </div>
        </div>
      </section>
    </main>
    <footer
      class="w-full border-t border-outline-variant dark:border-outline-variant px-margin md:px-margin-tablet lg:px-margin-desktop py-space-xl flex flex-col md:flex-row items-center justify-between gap-space-md bg-surface-container-lowest dark:bg-surface-container-lowest z-10"
    >
      <div class="flex flex-col items-center md:items-start gap-1">
        <div
          class="text-headline-sm font-headline-sm font-bold text-on-surface dark:text-on-surface flex items-center gap-space-xs"
        >
          <span
            class="material-symbols-outlined text-primary-container"
            data-icon="polyline"
            >polyline</span
          >
          <span>GeoMeasure API</span>
        </div>
        <p class="font-body-sm text-body-sm text-outline">
          Geospatial processing, built for developers.
        </p>
        <p class="font-code-sm text-code-sm text-outline mt-1">
          © 2026 GeoMeasure API. EPSG:4326/3857 Compliant.
        </p>
      </div>
      <!-- Links -->
      <div
        class="flex flex-wrap items-center justify-center gap-x-space-lg gap-y-2 text-on-surface-variant dark:text-on-surface-variant font-code-sm text-code-sm"
      >
        <a
          class="hover:text-primary dark:hover:text-primary transition-colors duration-150"
          href="/docs"
          rel="noreferrer"
          target="_blank"
        >
          Interactive Docs
        </a>
        <a
          class="hover:text-primary dark:hover:text-primary transition-colors duration-150"
          href="/redoc"
          rel="noreferrer"
          target="_blank"
        >
          ReDoc Reference
        </a>
        <a
          class="hover:text-primary dark:hover:text-primary transition-colors duration-150"
          href="/openapi.json"
          rel="noreferrer"
          target="_blank"
        >
          OpenAPI JSON
        </a>
        <a
          class="hover:text-primary dark:hover:text-primary transition-colors duration-150"
          href="#endpoints"
        >
          Endpoints
        </a>
        <a
          class="hover:text-primary dark:hover:text-primary transition-colors duration-150"
          href="#capabilities"
        >
          Vector Benchmarks
        </a>
      </div>
    </footer>
    <script>
      document.addEventListener("DOMContentLoaded", () => {
        const copyBtn = document.getElementById("copy-btn");
        const copyIcon = document.getElementById("copy-icon");
        const copyText = document.getElementById("copy-text");

        const rawGeoJson = `{
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [-0.12, 51.50],
        [-0.10, 51.50],
        [-0.10, 51.52],
        [-0.12, 51.52],
        [-0.12, 51.50]
      ]
    ]
  },
  "properties": {
    "measurement_unit": "meters"
  }
}`;

        if (copyBtn) {
          copyBtn.addEventListener("click", async () => {
            try {
              await navigator.clipboard.writeText(rawGeoJson);
              copyText.textContent = "Copied!";
              copyIcon.textContent = "check";
              copyBtn.classList.add("border-primary-container", "text-primary");

              setTimeout(() => {
                copyText.textContent = "Copy GeoJSON";
                copyIcon.textContent = "content_copy";
                copyBtn.classList.remove(
                  "border-primary-container",
                  "text-primary",
                );
              }, 2000);
            } catch (err) {
              console.error("Failed to copy", err);
            }
          });
        }
      });
    </script>
  </body>
</html>
"""

def render_landing(base_url: str) -> str:
    """Return the landing page with the public base URL filled in (HTML-escaped)."""
    return LANDING_TEMPLATE.replace("__BASE_URL__", escape(base_url.rstrip("/"), quote=True))