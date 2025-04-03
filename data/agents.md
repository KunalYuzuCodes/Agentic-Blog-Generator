<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/agents/">
      
      
        <link rel="prev" href="../troubleshooting/">
      
      
        <link rel="next" href="../models/">
      
      
      <link rel="icon" href="../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>Agents - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../extra/tweaks.css">
    
    <script>__md_scope=new URL("..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="Agents - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/agents.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/agents/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="Agents - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/agents.png">
      
    
    
   <link href="../assets/stylesheets/glightbox.min.css" rel="stylesheet"><style>
    html.glightbox-open { overflow: initial; height: 100%; }
    .gslide-title { margin-top: 0px; user-select: text; }
    .gslide-desc { color: #666; user-select: text; }
    .gslide-image img { background: white; }
    .gscrollbar-fixer { padding-right: 15px; }
    .gdesc-inner { font-size: 0.75rem; }
    body[data-md-color-scheme="slate"] .gdesc-inner { background: var(--md-default-bg-color);}
    body[data-md-color-scheme="slate"] .gslide-title { color: var(--md-default-fg-color);}
    body[data-md-color-scheme="slate"] .gslide-desc { color: var(--md-default-fg-color);}</style> <script src="../assets/javascripts/glightbox.min.js"></script><meta name="theme-color" content="#e92063"><meta name="color-scheme" content="light"></head>
  
  
    
    
      
    
    
    
    
    <body dir="ltr" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" data-md-color-media="(prefers-color-scheme)">
  
    
    <input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">
    <input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">
    <label class="md-overlay" for="__drawer"></label>
    <div data-md-component="skip">
      
        
        <a href="#introduction" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
    
      

  

<header class="md-header md-header--shadow" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href=".." title="PydanticAI" class="md-header__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../img/logo-white.svg" alt="logo">

    </a>
    <label class="md-header__button md-icon" for="__drawer">
      
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"></path></svg>
    </label>
    <div class="md-header__title" data-md-component="header-title">
      <div class="md-header__ellipsis">
        <div class="md-header__topic">
          <span class="md-ellipsis">
            PydanticAI
          </span>
        </div>
        <div class="md-header__topic" data-md-component="header-topic">
          <span class="md-ellipsis">
            
              Agents
            
          </span>
        </div>
      </div>
    </div>
    
      
        <form class="md-header__option" data-md-component="palette">
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme)" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to light mode" type="radio" name="__palette" id="__palette_0">
    
      <label class="md-header__button md-icon" title="Switch to light mode" for="__palette_1">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 2.38 1.19 4.47 3 5.74V17a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-2.26c1.81-1.27 3-3.36 3-5.74a7 7 0 0 0-7-7M9 21a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1v-1H9z"></path></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: light)" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to dark mode" type="radio" name="__palette" id="__palette_1">
    
      <label class="md-header__button md-icon" title="Switch to dark mode" for="__palette_2" hidden="">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 1 7 7c0 2.38-1.19 4.47-3 5.74V17a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1v-2.26C6.19 13.47 5 11.38 5 9a7 7 0 0 1 7-7M9 21v-1h6v1a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1m3-17a5 5 0 0 0-5 5c0 2.05 1.23 3.81 3 4.58V16h4v-2.42c1.77-.77 3-2.53 3-4.58a5 5 0 0 0-5-5"></path></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: dark)" data-md-color-scheme="slate" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to system preference" type="radio" name="__palette" id="__palette_2">
    
      <label class="md-header__button md-icon" title="Switch to system preference" for="__palette_0" hidden="">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9 2c3.87 0 7 3.13 7 7 0 2.38-1.19 4.47-3 5.74V17c0 .55-.45 1-1 1H6c-.55 0-1-.45-1-1v-2.26C3.19 13.47 2 11.38 2 9c0-3.87 3.13-7 7-7M6 21v-1h6v1c0 .55-.45 1-1 1H7c-.55 0-1-.45-1-1M9 4C6.24 4 4 6.24 4 9c0 2.05 1.23 3.81 3 4.58V16h4v-2.42c1.77-.77 3-2.53 3-4.58 0-2.76-2.24-5-5-5m10 9h-2l-3.2 9h1.9l.7-2h3.2l.7 2h1.9zm-2.15 5.65L18 15l1.15 3.65z"></path></svg>
      </label>
    
  
</form>
      
    
    
      <script>var palette=__md_get("__palette");if(palette&&palette.color){if("(prefers-color-scheme)"===palette.color.media){var media=matchMedia("(prefers-color-scheme: light)"),input=document.querySelector(media.matches?"[data-md-color-media='(prefers-color-scheme: light)']":"[data-md-color-media='(prefers-color-scheme: dark)']");palette.color.media=input.getAttribute("data-md-color-media"),palette.color.scheme=input.getAttribute("data-md-color-scheme"),palette.color.primary=input.getAttribute("data-md-color-primary"),palette.color.accent=input.getAttribute("data-md-color-accent")}for(var[key,value]of Object.entries(palette.color))document.body.setAttribute("data-md-color-"+key,value)}</script>
    
    
    
      <label class="md-header__button md-icon" for="__search">
        
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.52 6.52 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5"></path></svg>
      </label>
      <div class="md-search" role="dialog">
  <label class="md-search__overlay" for="__search"></label>
  <div class="md-search__inner" role="search">
    <form class="md-search__form" name="search">
      <input type="text" id="searchbox" class="md-search__input" name="query" aria-label="Search" placeholder="Search" autocapitalize="off" autocorrect="off" autocomplete="off" spellcheck="false" required="">
      <label class="md-search__icon md-icon" for="__search">

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.516 6.516 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5Z"></path></svg>

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 11v2H8l5.5 5.5-1.42 1.42L4.16 12l7.92-7.92L13.5 5.5 8 11h12Z"></path></svg>
      </label>
      <nav class="md-search__options" aria-label="Search">

        <button id="searchbox-clear" type="reset" class="md-search__icon md-icon" title="Clear" aria-label="Clear" tabindex="-1">

          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12 19 6.41Z"></path></svg>
        </button>
      </nav>

        <div class="md-search__suggest"></div>

    </form>
    <div class="md-search__output">
      <div class="md-search__scrollwrap" tabindex="0">
        <div class="md-search-result">
          <div class="md-search-result__meta" id="type-to-start-searching">Type to start searching</div>
          <ol class="md-search-result__list" id="hits" role="presentation" hidden=""></ol>
        </div>
      </div>
    </div>
  </div>
</div>
    
    
      <div class="md-header__source">
        <a href="https://github.com/pydantic/pydantic-ai" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository md-source__repository--active">
    pydantic/pydantic-ai
  <ul class="md-source__facts"><li class="md-source__fact md-source__fact--version">v0.0.50</li><li class="md-source__fact md-source__fact--stars">8k</li><li class="md-source__fact md-source__fact--forks">687</li></ul></div>
</a>
      </div>
    
  </nav>
  
</header>
    
    <div class="md-container" data-md-component="container">
      
      
        
          
        
      
      <main class="md-main" data-md-component="main">
        <div class="md-main__inner md-grid">
          
            
              
              <div class="md-sidebar md-sidebar--primary" data-md-component="sidebar" data-md-type="navigation">
                <div class="md-sidebar__scrollwrap">
                  <div class="md-sidebar__inner">
                    



<nav class="md-nav md-nav--primary" aria-label="Navigation" data-md-level="0">
  <label class="md-nav__title" for="__drawer">
    <a href=".." title="PydanticAI" class="md-nav__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../img/logo-white.svg" alt="logo">

    </a>
    PydanticAI
  </label>
  
    <div class="md-nav__source">
      <a href="https://github.com/pydantic/pydantic-ai" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository md-source__repository--active">
    pydantic/pydantic-ai
  <ul class="md-source__facts"><li class="md-source__fact md-source__fact--version">v0.0.50</li><li class="md-source__fact md-source__fact--stars">8k</li><li class="md-source__fact md-source__fact--forks">687</li></ul></div>
</a>
    </div>
  
  <ul class="md-nav__list">
    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href=".." class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Introduction
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../install/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Installation
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../help/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Getting Help
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../contributing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Contributing
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../troubleshooting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Troubleshooting
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
    
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6" checked="">
        
          
          <label class="md-nav__link" for="__nav_6" id="__nav_6_label" tabindex="">
            
  
  <span class="md-ellipsis">
    Documentation
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_6_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_6">
            <span class="md-nav__icon md-icon"></span>
            Documentation
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#introduction" class="md-nav__link">
    <span class="md-ellipsis">
      Introduction
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#running-agents" class="md-nav__link">
    <span class="md-ellipsis">
      Running Agents
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Running Agents">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#iterating-over-an-agents-graph" class="md-nav__link">
    <span class="md-ellipsis">
      Iterating Over an Agent's Graph
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Iterating Over an Agent's Graph">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#async-for-iteration" class="md-nav__link">
    <span class="md-ellipsis">
      async for iteration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#using-next-manually" class="md-nav__link">
    <span class="md-ellipsis">
      Using .next(...) manually
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#accessing-usage-and-the-final-result" class="md-nav__link">
    <span class="md-ellipsis">
      Accessing usage and the final result
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
        
          <li class="md-nav__item">
  <a href="#streaming" class="md-nav__link">
    <span class="md-ellipsis">
      Streaming
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#additional-configuration" class="md-nav__link">
    <span class="md-ellipsis">
      Additional Configuration
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Additional Configuration">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#usage-limits" class="md-nav__link">
    <span class="md-ellipsis">
      Usage Limits
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#model-run-settings" class="md-nav__link">
    <span class="md-ellipsis">
      Model (Run) Settings
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
        
          <li class="md-nav__item">
  <a href="#model-specific-settings" class="md-nav__link">
    <span class="md-ellipsis">
      Model specific settings
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#runs-vs-conversations" class="md-nav__link">
    <span class="md-ellipsis">
      Runs vs. Conversations
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#static-type-checking" class="md-nav__link">
    <span class="md-ellipsis">
      Type safe by design
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#system-prompts" class="md-nav__link">
    <span class="md-ellipsis">
      System Prompts
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#reflection-and-self-correction" class="md-nav__link">
    <span class="md-ellipsis">
      Reflection and self-correction
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#model-errors" class="md-nav__link">
    <span class="md-ellipsis">
      Model errors
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../dependencies/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Dependencies
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Function Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../common-tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Common Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../results/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Results
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../message-history/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Messages and chat history
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../testing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Unit testing
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../logfire/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Debugging and Monitoring
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../multi-agent-applications/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Multi-agent Applications
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Graphs
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../evals/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Evals
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../input/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Image, Audio &amp; Document Input
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_14">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../mcp/" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    MCP
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_6_14" id="__nav_6_14_label" tabindex="0">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_6_14_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_6_14">
            <span class="md-nav__icon md-icon"></span>
            MCP
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/client/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Client
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/server/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Server
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/run-python/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    MCP Run Python
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../cli/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Command Line Interface (CLI)
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_7">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../examples/" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    Examples
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_7" id="__nav_7_label" tabindex="">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_7_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_7">
            <span class="md-nav__icon md-icon"></span>
            Examples
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/pydantic-model/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Pydantic Model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/weather-agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Weather agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/bank-support/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Bank support
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/sql-gen/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    SQL Generation
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/flight-booking/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Flight booking
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/rag/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    RAG
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/stream-markdown/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream markdown
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/stream-whales/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream whales
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/chat-app/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Chat App with FastAPI
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/question-graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Question Graph
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_8">
        
          
          <label class="md-nav__link" for="__nav_8" id="__nav_8_label" tabindex="">
            
  
  <span class="md-ellipsis">
    API Reference
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_8_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_8">
            <span class="md-nav__icon md-icon"></span>
            API Reference
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/common_tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.common_tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/result/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/messages/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/settings/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.settings
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/usage/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.usage
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/mcp/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.mcp
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/format_as_xml/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.format_as_xml
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/base/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/openai/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.openai
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/anthropic/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.anthropic
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/bedrock/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.bedrock
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/cohere/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.cohere
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/gemini/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.gemini
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/groq/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.groq
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/instrumented/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/mistral/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.test
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/function/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/fallback/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/wrapper/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.wrapper
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/providers/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.providers
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/nodes/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.nodes
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/persistence/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/mermaid/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/dataset/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/evaluators/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/generation/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.generation
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
  </ul>
</nav>
                  </div>
                </div>
              </div>
            
            
              
              <div class="md-sidebar md-sidebar--secondary" data-md-component="sidebar" data-md-type="toc" style="top: 48px;">
                <div class="md-sidebar__scrollwrap" style="height: 474px;">
                  <div class="md-sidebar__inner">
                    

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#introduction" class="md-nav__link">
    <span class="md-ellipsis">
      Introduction
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#running-agents" class="md-nav__link">
    <span class="md-ellipsis">
      Running Agents
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Running Agents">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#iterating-over-an-agents-graph" class="md-nav__link">
    <span class="md-ellipsis">
      Iterating Over an Agent's Graph
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Iterating Over an Agent's Graph">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#async-for-iteration" class="md-nav__link">
    <span class="md-ellipsis">
      async for iteration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#using-next-manually" class="md-nav__link">
    <span class="md-ellipsis">
      Using .next(...) manually
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#accessing-usage-and-the-final-result" class="md-nav__link">
    <span class="md-ellipsis">
      Accessing usage and the final result
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
        
          <li class="md-nav__item">
  <a href="#streaming" class="md-nav__link">
    <span class="md-ellipsis">
      Streaming
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#additional-configuration" class="md-nav__link">
    <span class="md-ellipsis">
      Additional Configuration
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Additional Configuration">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#usage-limits" class="md-nav__link">
    <span class="md-ellipsis">
      Usage Limits
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#model-run-settings" class="md-nav__link">
    <span class="md-ellipsis">
      Model (Run) Settings
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
        
          <li class="md-nav__item">
  <a href="#model-specific-settings" class="md-nav__link">
    <span class="md-ellipsis">
      Model specific settings
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#runs-vs-conversations" class="md-nav__link">
    <span class="md-ellipsis">
      Runs vs. Conversations
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#static-type-checking" class="md-nav__link">
    <span class="md-ellipsis">
      Type safe by design
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#system-prompts" class="md-nav__link">
    <span class="md-ellipsis">
      System Prompts
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#reflection-and-self-correction" class="md-nav__link">
    <span class="md-ellipsis">
      Reflection and self-correction
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#model-errors" class="md-nav__link">
    <span class="md-ellipsis">
      Model errors
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
                  </div>
                </div>
              </div>
            
          
          
            <div class="md-content" data-md-component="content">
              <article class="md-content__inner md-typeset">
                
                  


  
  


  <h1>Agents</h1>

<h2 id="introduction">Introduction</h2>
<p>Agents are PydanticAI's primary interface for interacting with LLMs.</p>
<p>In some use cases a single Agent will control an entire application or component,
but multiple agents can also interact to embody more complex workflows.</p>
<p>The <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent"><code>Agent</code></a> class has full API documentation, but conceptually you can think of an agent as a container for:</p>
<div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
<thead>
<tr>
<th><strong>Component</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#system-prompts">System prompt(s)</a></td>
<td>A set of instructions for the LLM written by the developer.</td>
</tr>
<tr>
<td><a href="../tools/">Function tool(s)</a></td>
<td>Functions that the LLM may call to get information while generating a response.</td>
</tr>
<tr>
<td><a href="../results/">Structured result type</a></td>
<td>The structured datatype the LLM must return at the end of a run, if specified.</td>
</tr>
<tr>
<td><a href="../dependencies/">Dependency type constraint</a></td>
<td>System prompt functions, tools, and result validators may all use dependencies when they're run.</td>
</tr>
<tr>
<td><a href="../api/models/base/">LLM model</a></td>
<td>Optional default LLM model associated with the agent. Can also be specified when running the agent.</td>
</tr>
<tr>
<td><a href="#additional-configuration">Model Settings</a></td>
<td>Optional default model settings to help fine tune requests. Can also be specified when running the agent.</td>
</tr>
</tbody>
</table></div></div>
<p>In typing terms, agents are generic in their dependency and result types, e.g., an agent which required dependencies of type <code class="language-python highlight"><span class="n">Foobar</span></code> and returned results of type <code class="language-python highlight"><span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span></code> would have type <code>Agent[Foobar, list[str]]</code>. In practice, you shouldn't need to care about this, it should just mean your IDE can tell you when you have the right type, and if you choose to use <a href="#static-type-checking">static type checking</a> it should work well with PydanticAI.</p>
<p>Here's a toy example of an agent that simulates a roulette wheel:</p>
<div class="language-python highlight"><span class="filename">roulette_wheel.py</span><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span><span class="p">,</span> <span class="n">RunContext</span>

<span class="n">roulette_agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 232px; --md-tooltip-y: 58px; --md-tooltip-0: -16px;"><a href="#__code_0_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
    <span class="s1">'openai:gpt-4o'</span><span class="p">,</span>
    <span class="n">deps_type</span><span class="o">=</span><span class="nb">int</span><span class="p">,</span>
    <span class="n">result_type</span><span class="o">=</span><span class="nb">bool</span><span class="p">,</span>
    <span class="n">system_prompt</span><span class="o">=</span><span class="p">(</span>
        <span class="s1">'Use the `roulette_wheel` function to see if the '</span>
        <span class="s1">'customer has won based on the number they provide.'</span>
    <span class="p">),</span>
<span class="p">)</span>


<span class="nd">@roulette_agent</span><span class="o">.</span><span class="n">tool</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">roulette_wheel</span><span class="p">(</span><span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="nb">int</span><span class="p">],</span> <span class="n">square</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 591px; --md-tooltip-y: 287px; --md-tooltip-0: -16px;"><a href="#__code_0_annotation_2" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="2"></span></a></aside></span>
<span class="w">    </span><span class="sd">"""check if the square is a winner"""</span>
    <span class="k">return</span> <span class="s1">'winner'</span> <span class="k">if</span> <span class="n">square</span> <span class="o">==</span> <span class="n">ctx</span><span class="o">.</span><span class="n">deps</span> <span class="k">else</span> <span class="s1">'loser'</span>


<span class="c1"># Run the agent</span>
<span class="n">success_number</span> <span class="o">=</span> <span class="mi">18</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 199px; --md-tooltip-y: 401px; --md-tooltip-0: -16px;"><a href="#__code_0_annotation_3" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="3"></span></a></aside></span>
<span class="n">result</span> <span class="o">=</span> <span class="n">roulette_agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'Put my money on square eighteen'</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="n">success_number</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 191px; --md-tooltip-y: 439px; --md-tooltip-0: -16px;"><a href="#__code_0_annotation_4" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="4"></span></a></aside></span>
<span class="c1">#&gt; True</span>

<span class="n">result</span> <span class="o">=</span> <span class="n">roulette_agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'I bet five is the winner'</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="n">success_number</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; False</span>
</code></pre></div>
<ol hidden="">
<li></li>
<li></li>
<li></li>
<li></li>
</ol>
<div class="admonition tip">
<p class="admonition-title">Agents are designed for reuse, like FastAPI Apps</p>
<p>Agents are intended to be instantiated once (frequently as module globals) and reused throughout your application, similar to a small <a class="autorefs autorefs-external" href="https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI">FastAPI</a> app or an <a class="autorefs autorefs-external" href="https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter">APIRouter</a>.</p>
</div>
<h2 id="running-agents">Running Agents</h2>
<p>There are four ways to run an agent:</p>
<ol>
<li><a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent.run"><code>agent.run()</code></a> — a coroutine which returns a <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.AgentRunResult"><code>RunResult</code></a> containing a completed response.</li>
<li><a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent.run_sync"><code>agent.run_sync()</code></a> — a plain, synchronous function which returns a <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.AgentRunResult"><code>RunResult</code></a> containing a completed response (internally, this just calls <code>loop.run_until_complete(self.run())</code>).</li>
<li><a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent.run_stream"><code>agent.run_stream()</code></a> — a coroutine which returns a <a class="autorefs autorefs-internal" href="../api/result/#pydantic_ai.result.StreamedRunResult"><code>StreamedRunResult</code></a>, which contains methods to stream a response as an async iterable.</li>
<li><a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent.iter"><code>agent.iter()</code></a> — a context manager which returns an <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.AgentRun"><code>AgentRun</code></a>, an async-iterable over the nodes of the agent's underlying <a class="autorefs autorefs-internal" href="../api/pydantic_graph/graph/#pydantic_graph.graph.Graph"><code>Graph</code></a>.</li>
</ol>
<p>Here's a simple example demonstrating the first three:</p>
<p></p><div class="language-python highlight"><span class="filename">run_agent.py</span><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'openai:gpt-4o'</span><span class="p">)</span>

<span class="n">result_sync</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'What is the capital of Italy?'</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result_sync</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; Rome</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">agent</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="s1">'What is the capital of France?'</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
    <span class="c1">#&gt; Paris</span>

    <span class="k">async</span> <span class="k">with</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_stream</span><span class="p">(</span><span class="s1">'What is the capital of the UK?'</span><span class="p">)</span> <span class="k">as</span> <span class="n">response</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="k">await</span> <span class="n">response</span><span class="o">.</span><span class="n">get_data</span><span class="p">())</span>
        <span class="c1">#&gt; London</span>
</code></pre></div>
<em>(This example is complete, it can be run "as is" — you'll need to add <code>asyncio.run(main())</code> to run <code>main</code>)</em><p></p>
<p>You can also pass messages from previous runs to continue a conversation or provide context, as described in <a href="../message-history/">Messages and Chat History</a>.</p>
<h3 id="iterating-over-an-agents-graph">Iterating Over an Agent's Graph</h3>
<p>Under the hood, each <code>Agent</code> in PydanticAI uses <strong>pydantic-graph</strong> to manage its execution flow. <strong>pydantic-graph</strong> is a generic, type-centric library for building and running finite state machines in Python. It doesn't actually depend on PydanticAI — you can use it standalone for workflows that have nothing to do with GenAI — but PydanticAI makes use of it to orchestrate the handling of model requests and model responses in an agent's run.</p>
<p>In many scenarios, you don't need to worry about pydantic-graph at all; calling <code>agent.run(...)</code> simply traverses the underlying graph from start to finish. However, if you need deeper insight or control — for example to capture each tool invocation, or to inject your own logic at specific stages — PydanticAI exposes the lower-level iteration process via <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent.iter"><code>Agent.iter</code></a>. This method returns an <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.AgentRun"><code>AgentRun</code></a>, which you can async-iterate over, or manually drive node-by-node via the <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.AgentRun.next"><code>next</code></a> method. Once the agent's graph returns an <a class="autorefs autorefs-internal" href="../api/pydantic_graph/nodes/#pydantic_graph.nodes.End"><code>End</code></a>, you have the final result along with a detailed history of all steps.</p>
<h4 id="async-for-iteration"><code>async for</code> iteration</h4>
<p>Here's an example of using <code>async for</code> with <code>iter</code> to record each node the agent executes:</p>
<div class="language-python highlight"><span class="filename">agent_iter_async_for.py</span><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'openai:gpt-4o'</span><span class="p">)</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="c1"># Begin an AgentRun, which is an async-iterable over the nodes of the agent's graph</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">agent</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="s1">'What is the capital of France?'</span><span class="p">)</span> <span class="k">as</span> <span class="n">agent_run</span><span class="p">:</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">agent_run</span><span class="p">:</span>
            <span class="c1"># Each node represents a step in the agent's execution</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    [</span>
<span class="sd">        ModelRequestNode(</span>
<span class="sd">            request=ModelRequest(</span>
<span class="sd">                parts=[</span>
<span class="sd">                    UserPromptPart(</span>
<span class="sd">                        content='What is the capital of France?',</span>
<span class="sd">                        timestamp=datetime.datetime(...),</span>
<span class="sd">                        part_kind='user-prompt',</span>
<span class="sd">                    )</span>
<span class="sd">                ],</span>
<span class="sd">                kind='request',</span>
<span class="sd">            )</span>
<span class="sd">        ),</span>
<span class="sd">        CallToolsNode(</span>
<span class="sd">            model_response=ModelResponse(</span>
<span class="sd">                parts=[TextPart(content='Paris', part_kind='text')],</span>
<span class="sd">                model_name='gpt-4o',</span>
<span class="sd">                timestamp=datetime.datetime(...),</span>
<span class="sd">                kind='response',</span>
<span class="sd">            )</span>
<span class="sd">        ),</span>
<span class="sd">        End(data=FinalResult(data='Paris', tool_name=None, tool_call_id=None)),</span>
<span class="sd">    ]</span>
<span class="sd">    """</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">agent_run</span><span class="o">.</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
    <span class="c1">#&gt; Paris</span>
</code></pre></div>
<ul>
<li>The <code>AgentRun</code> is an async iterator that yields each node (<code>BaseNode</code> or <code>End</code>) in the flow.</li>
<li>The run ends when an <code>End</code> node is returned.</li>
</ul>
<h4 id="using-next-manually">Using <code>.next(...)</code> manually</h4>
<p>You can also drive the iteration manually by passing the node you want to run next to the <code>AgentRun.next(...)</code> method. This allows you to inspect or modify the node before it executes or skip nodes based on your own logic, and to catch errors in <code>next()</code> more easily:</p>
<div class="language-python highlight"><span class="filename">agent_iter_next.py</span><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_graph</span><span class="w"> </span><span class="kn">import</span> <span class="n">End</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'openai:gpt-4o'</span><span class="p">)</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">agent</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="s1">'What is the capital of France?'</span><span class="p">)</span> <span class="k">as</span> <span class="n">agent_run</span><span class="p">:</span>
        <span class="n">node</span> <span class="o">=</span> <span class="n">agent_run</span><span class="o">.</span><span class="n">next_node</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 322px; --md-tooltip-y: 172px; --md-tooltip-0: -16px;"><a href="#__code_3_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>

        <span class="n">all_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">node</span><span class="p">]</span>

        <span class="c1"># Drive the iteration manually:</span>
        <span class="k">while</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">End</span><span class="p">):</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 371px; --md-tooltip-y: 268px; --md-tooltip-0: -16px;"><a href="#__code_3_annotation_2" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="2"></span></a></aside></span>
            <span class="n">node</span> <span class="o">=</span> <span class="k">await</span> <span class="n">agent_run</span><span class="o">.</span><span class="n">next</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 412px; --md-tooltip-y: 287px; --md-tooltip-0: -16px;"><a href="#__code_3_annotation_3" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="3"></span></a></aside></span>
            <span class="n">all_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 322px; --md-tooltip-y: 306px; --md-tooltip-0: -16px;"><a href="#__code_3_annotation_4" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="4"></span></a></aside></span>

        <span class="nb">print</span><span class="p">(</span><span class="n">all_nodes</span><span class="p">)</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        [</span>
<span class="sd">            UserPromptNode(</span>
<span class="sd">                user_prompt='What is the capital of France?',</span>
<span class="sd">                system_prompts=(),</span>
<span class="sd">                system_prompt_functions=[],</span>
<span class="sd">                system_prompt_dynamic_functions={},</span>
<span class="sd">            ),</span>
<span class="sd">            ModelRequestNode(</span>
<span class="sd">                request=ModelRequest(</span>
<span class="sd">                    parts=[</span>
<span class="sd">                        UserPromptPart(</span>
<span class="sd">                            content='What is the capital of France?',</span>
<span class="sd">                            timestamp=datetime.datetime(...),</span>
<span class="sd">                            part_kind='user-prompt',</span>
<span class="sd">                        )</span>
<span class="sd">                    ],</span>
<span class="sd">                    kind='request',</span>
<span class="sd">                )</span>
<span class="sd">            ),</span>
<span class="sd">            CallToolsNode(</span>
<span class="sd">                model_response=ModelResponse(</span>
<span class="sd">                    parts=[TextPart(content='Paris', part_kind='text')],</span>
<span class="sd">                    model_name='gpt-4o',</span>
<span class="sd">                    timestamp=datetime.datetime(...),</span>
<span class="sd">                    kind='response',</span>
<span class="sd">                )</span>
<span class="sd">            ),</span>
<span class="sd">            End(data=FinalResult(data='Paris', tool_name=None, tool_call_id=None)),</span>
<span class="sd">        ]</span>
<span class="sd">        """</span>
</code></pre></div>
<ol hidden="">
<li></li>
<li></li>
<li></li>
<li></li>
</ol>
<h4 id="accessing-usage-and-the-final-result">Accessing usage and the final result</h4>
<p>You can retrieve usage statistics (tokens, requests, etc.) at any time from the <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.AgentRun"><code>AgentRun</code></a> object via <code>agent_run.usage()</code>. This method returns a <a class="autorefs autorefs-internal" href="../api/usage/#pydantic_ai.usage.Usage"><code>Usage</code></a> object containing the usage data.</p>
<p>Once the run finishes, <code>agent_run.final_result</code> becomes a <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.AgentRunResult"><code>AgentRunResult</code></a> object containing the final output (and related metadata).</p>
<hr>
<h3 id="streaming">Streaming</h3>
<p>Here is an example of streaming an agent run in combination with <code>async for</code> iteration:</p>
<div class="language-python highlight"><span class="filename">streaming.py</span><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code tabindex="0"><span class="kn">import</span><span class="w"> </span><span class="nn">asyncio</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">dataclasses</span><span class="w"> </span><span class="kn">import</span> <span class="n">dataclass</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">datetime</span><span class="w"> </span><span class="kn">import</span> <span class="n">date</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.messages</span><span class="w"> </span><span class="kn">import</span> <span class="p">(</span>
    <span class="n">FinalResultEvent</span><span class="p">,</span>
    <span class="n">FunctionToolCallEvent</span><span class="p">,</span>
    <span class="n">FunctionToolResultEvent</span><span class="p">,</span>
    <span class="n">PartDeltaEvent</span><span class="p">,</span>
    <span class="n">PartStartEvent</span><span class="p">,</span>
    <span class="n">TextPartDelta</span><span class="p">,</span>
    <span class="n">ToolCallPartDelta</span><span class="p">,</span>
<span class="p">)</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.tools</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunContext</span>


<span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">WeatherService</span><span class="p">:</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">get_forecast</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">location</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">forecast_date</span><span class="p">:</span> <span class="n">date</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="c1"># In real code: call weather API, DB queries, etc.</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s1">'The forecast in </span><span class="si">{</span><span class="n">location</span><span class="si">}</span><span class="s1"> on </span><span class="si">{</span><span class="n">forecast_date</span><span class="si">}</span><span class="s1"> is 24°C and sunny.'</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">get_historic_weather</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">location</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">forecast_date</span><span class="p">:</span> <span class="n">date</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="c1"># In real code: call a historical weather API or DB</span>
        <span class="k">return</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s1">'The weather in </span><span class="si">{</span><span class="n">location</span><span class="si">}</span><span class="s1"> on </span><span class="si">{</span><span class="n">forecast_date</span><span class="si">}</span><span class="s1"> was 18°C and partly cloudy.'</span>
        <span class="p">)</span>


<span class="n">weather_agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">[</span><span class="n">WeatherService</span><span class="p">,</span> <span class="nb">str</span><span class="p">](</span>
    <span class="s1">'openai:gpt-4o'</span><span class="p">,</span>
    <span class="n">deps_type</span><span class="o">=</span><span class="n">WeatherService</span><span class="p">,</span>
    <span class="n">result_type</span><span class="o">=</span><span class="nb">str</span><span class="p">,</span>  <span class="c1"># We'll produce a final answer as plain text</span>
    <span class="n">system_prompt</span><span class="o">=</span><span class="s1">'Providing a weather forecast at the locations the user provides.'</span><span class="p">,</span>
<span class="p">)</span>


<span class="nd">@weather_agent</span><span class="o">.</span><span class="n">tool</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">weather_forecast</span><span class="p">(</span>
    <span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="n">WeatherService</span><span class="p">],</span>
    <span class="n">location</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">forecast_date</span><span class="p">:</span> <span class="n">date</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">forecast_date</span> <span class="o">&gt;=</span> <span class="n">date</span><span class="o">.</span><span class="n">today</span><span class="p">():</span>
        <span class="k">return</span> <span class="k">await</span> <span class="n">ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">get_forecast</span><span class="p">(</span><span class="n">location</span><span class="p">,</span> <span class="n">forecast_date</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="k">await</span> <span class="n">ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">get_historic_weather</span><span class="p">(</span><span class="n">location</span><span class="p">,</span> <span class="n">forecast_date</span><span class="p">)</span>


<span class="n">output_messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="n">user_prompt</span> <span class="o">=</span> <span class="s1">'What will the weather be like in Paris on Tuesday?'</span>

    <span class="c1"># Begin a node-by-node, streaming iteration</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">weather_agent</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="n">user_prompt</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="n">WeatherService</span><span class="p">())</span> <span class="k">as</span> <span class="n">run</span><span class="p">:</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">run</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">Agent</span><span class="o">.</span><span class="n">is_user_prompt_node</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
                <span class="c1"># A user prompt node =&gt; The user has provided input</span>
                <span class="n">output_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">'=== UserPromptNode: </span><span class="si">{</span><span class="n">node</span><span class="o">.</span><span class="n">user_prompt</span><span class="si">}</span><span class="s1"> ==='</span><span class="p">)</span>
            <span class="k">elif</span> <span class="n">Agent</span><span class="o">.</span><span class="n">is_model_request_node</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
                <span class="c1"># A model request node =&gt; We can stream tokens from the model's request</span>
                <span class="n">output_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="s1">'=== ModelRequestNode: streaming partial request tokens ==='</span>
                <span class="p">)</span>
                <span class="k">async</span> <span class="k">with</span> <span class="n">node</span><span class="o">.</span><span class="n">stream</span><span class="p">(</span><span class="n">run</span><span class="o">.</span><span class="n">ctx</span><span class="p">)</span> <span class="k">as</span> <span class="n">request_stream</span><span class="p">:</span>
                    <span class="k">async</span> <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">request_stream</span><span class="p">:</span>
                        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">event</span><span class="p">,</span> <span class="n">PartStartEvent</span><span class="p">):</span>
                            <span class="n">output_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                                <span class="sa">f</span><span class="s1">'[Request] Starting part </span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">index</span><span class="si">}</span><span class="s1">: </span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">part</span><span class="si">!r}</span><span class="s1">'</span>
                            <span class="p">)</span>
                        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">event</span><span class="p">,</span> <span class="n">PartDeltaEvent</span><span class="p">):</span>
                            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">delta</span><span class="p">,</span> <span class="n">TextPartDelta</span><span class="p">):</span>
                                <span class="n">output_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                                    <span class="sa">f</span><span class="s1">'[Request] Part </span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">index</span><span class="si">}</span><span class="s1"> text delta: </span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">delta</span><span class="o">.</span><span class="n">content_delta</span><span class="si">!r}</span><span class="s1">'</span>
                                <span class="p">)</span>
                            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">delta</span><span class="p">,</span> <span class="n">ToolCallPartDelta</span><span class="p">):</span>
                                <span class="n">output_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                                    <span class="sa">f</span><span class="s1">'[Request] Part </span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">index</span><span class="si">}</span><span class="s1"> args_delta=</span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">delta</span><span class="o">.</span><span class="n">args_delta</span><span class="si">}</span><span class="s1">'</span>
                                <span class="p">)</span>
                        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">event</span><span class="p">,</span> <span class="n">FinalResultEvent</span><span class="p">):</span>
                            <span class="n">output_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                                <span class="sa">f</span><span class="s1">'[Result] The model produced a final result (tool_name=</span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">tool_name</span><span class="si">}</span><span class="s1">)'</span>
                            <span class="p">)</span>
            <span class="k">elif</span> <span class="n">Agent</span><span class="o">.</span><span class="n">is_call_tools_node</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
                <span class="c1"># A handle-response node =&gt; The model returned some data, potentially calls a tool</span>
                <span class="n">output_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="s1">'=== CallToolsNode: streaming partial response &amp; tool usage ==='</span>
                <span class="p">)</span>
                <span class="k">async</span> <span class="k">with</span> <span class="n">node</span><span class="o">.</span><span class="n">stream</span><span class="p">(</span><span class="n">run</span><span class="o">.</span><span class="n">ctx</span><span class="p">)</span> <span class="k">as</span> <span class="n">handle_stream</span><span class="p">:</span>
                    <span class="k">async</span> <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">handle_stream</span><span class="p">:</span>
                        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">event</span><span class="p">,</span> <span class="n">FunctionToolCallEvent</span><span class="p">):</span>
                            <span class="n">output_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                                <span class="sa">f</span><span class="s1">'[Tools] The LLM calls tool=</span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">part</span><span class="o">.</span><span class="n">tool_name</span><span class="si">!r}</span><span class="s1"> with args=</span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">part</span><span class="o">.</span><span class="n">args</span><span class="si">}</span><span class="s1"> (tool_call_id=</span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">part</span><span class="o">.</span><span class="n">tool_call_id</span><span class="si">!r}</span><span class="s1">)'</span>
                            <span class="p">)</span>
                        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">event</span><span class="p">,</span> <span class="n">FunctionToolResultEvent</span><span class="p">):</span>
                            <span class="n">output_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                                <span class="sa">f</span><span class="s1">'[Tools] Tool call </span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">tool_call_id</span><span class="si">!r}</span><span class="s1"> returned =&gt; </span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">result</span><span class="o">.</span><span class="n">content</span><span class="si">}</span><span class="s1">'</span>
                            <span class="p">)</span>
            <span class="k">elif</span> <span class="n">Agent</span><span class="o">.</span><span class="n">is_end_node</span><span class="p">(</span><span class="n">node</span><span class="p">):</span>
                <span class="k">assert</span> <span class="n">run</span><span class="o">.</span><span class="n">result</span><span class="o">.</span><span class="n">data</span> <span class="o">==</span> <span class="n">node</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">data</span>
                <span class="c1"># Once an End node is reached, the agent run is complete</span>
                <span class="n">output_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">'=== Final Agent Output: </span><span class="si">{</span><span class="n">run</span><span class="o">.</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="si">}</span><span class="s1"> ==='</span><span class="p">)</span>


<span class="k">if</span> <span class="vm">__name__</span> <span class="o">==</span> <span class="s1">'__main__'</span><span class="p">:</span>
    <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">main</span><span class="p">())</span>

    <span class="nb">print</span><span class="p">(</span><span class="n">output_messages</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    [</span>
<span class="sd">        '=== ModelRequestNode: streaming partial request tokens ===',</span>
<span class="sd">        '[Request] Starting part 0: ToolCallPart(tool_name=\'weather_forecast\', args=\'{"location":"Pa\', tool_call_id=\'0001\', part_kind=\'tool-call\')',</span>
<span class="sd">        '[Request] Part 0 args_delta=ris","forecast_',</span>
<span class="sd">        '[Request] Part 0 args_delta=date":"2030-01-',</span>
<span class="sd">        '[Request] Part 0 args_delta=01"}',</span>
<span class="sd">        '=== CallToolsNode: streaming partial response &amp; tool usage ===',</span>
<span class="sd">        '[Tools] The LLM calls tool=\'weather_forecast\' with args={"location":"Paris","forecast_date":"2030-01-01"} (tool_call_id=\'0001\')',</span>
<span class="sd">        "[Tools] Tool call '0001' returned =&gt; The forecast in Paris on 2030-01-01 is 24°C and sunny.",</span>
<span class="sd">        '=== ModelRequestNode: streaming partial request tokens ===',</span>
<span class="sd">        "[Request] Starting part 0: TextPart(content='It will be ', part_kind='text')",</span>
<span class="sd">        '[Result] The model produced a final result (tool_name=None)',</span>
<span class="sd">        "[Request] Part 0 text delta: 'warm and sunny '",</span>
<span class="sd">        "[Request] Part 0 text delta: 'in Paris on '",</span>
<span class="sd">        "[Request] Part 0 text delta: 'Tuesday.'",</span>
<span class="sd">        '=== CallToolsNode: streaming partial response &amp; tool usage ===',</span>
<span class="sd">        '=== Final Agent Output: It will be warm and sunny in Paris on Tuesday. ===',</span>
<span class="sd">    ]</span>
<span class="sd">    """</span>
</code></pre></div>
<hr>
<h3 id="additional-configuration">Additional Configuration</h3>
<h4 id="usage-limits">Usage Limits</h4>
<p>PydanticAI offers a <a class="autorefs autorefs-internal" href="../api/usage/#pydantic_ai.usage.UsageLimits"><code>UsageLimits</code></a> structure to help you limit your
usage (tokens and/or requests) on model runs.</p>
<p>You can apply these settings by passing the <code>usage_limits</code> argument to the <code>run{_sync,_stream}</code> functions.</p>
<p>Consider the following example, where we limit the number of response tokens:</p>
<div class="language-py highlight"><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.exceptions</span><span class="w"> </span><span class="kn">import</span> <span class="n">UsageLimitExceeded</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.usage</span><span class="w"> </span><span class="kn">import</span> <span class="n">UsageLimits</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'anthropic:claude-3-5-sonnet-latest'</span><span class="p">)</span>

<span class="n">result_sync</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span>
    <span class="s1">'What is the capital of Italy? Answer with just the city.'</span><span class="p">,</span>
    <span class="n">usage_limits</span><span class="o">=</span><span class="n">UsageLimits</span><span class="p">(</span><span class="n">response_tokens_limit</span><span class="o">=</span><span class="mi">10</span><span class="p">),</span>
<span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result_sync</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; Rome</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result_sync</span><span class="o">.</span><span class="n">usage</span><span class="p">())</span>
<span class="sd">"""</span>
<span class="sd">Usage(requests=1, request_tokens=62, response_tokens=1, total_tokens=63, details=None)</span>
<span class="sd">"""</span>

<span class="k">try</span><span class="p">:</span>
    <span class="n">result_sync</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span>
        <span class="s1">'What is the capital of Italy? Answer with a paragraph.'</span><span class="p">,</span>
        <span class="n">usage_limits</span><span class="o">=</span><span class="n">UsageLimits</span><span class="p">(</span><span class="n">response_tokens_limit</span><span class="o">=</span><span class="mi">10</span><span class="p">),</span>
    <span class="p">)</span>
<span class="k">except</span> <span class="n">UsageLimitExceeded</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">e</span><span class="p">)</span>
    <span class="c1">#&gt; Exceeded the response_tokens_limit of 10 (response_tokens=32)</span>
</code></pre></div>
<p>Restricting the number of requests can be useful in preventing infinite loops or excessive tool calling:</p>
<div class="language-py highlight"><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code tabindex="0"><span class="kn">from</span><span class="w"> </span><span class="nn">typing_extensions</span><span class="w"> </span><span class="kn">import</span> <span class="n">TypedDict</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span><span class="p">,</span> <span class="n">ModelRetry</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.exceptions</span><span class="w"> </span><span class="kn">import</span> <span class="n">UsageLimitExceeded</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.usage</span><span class="w"> </span><span class="kn">import</span> <span class="n">UsageLimits</span>


<span class="k">class</span><span class="w"> </span><span class="nc">NeverResultType</span><span class="p">(</span><span class="n">TypedDict</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Never ever coerce data to this type.</span>
<span class="sd">    """</span>

    <span class="n">never_use_this</span><span class="p">:</span> <span class="nb">str</span>


<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
    <span class="s1">'anthropic:claude-3-5-sonnet-latest'</span><span class="p">,</span>
    <span class="n">retries</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
    <span class="n">result_type</span><span class="o">=</span><span class="n">NeverResultType</span><span class="p">,</span>
    <span class="n">system_prompt</span><span class="o">=</span><span class="s1">'Any time you get a response, call the `infinite_retry_tool` to produce another response.'</span><span class="p">,</span>
<span class="p">)</span>


<span class="nd">@agent</span><span class="o">.</span><span class="n">tool_plain</span><span class="p">(</span><span class="n">retries</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 273px; --md-tooltip-y: 458px; --md-tooltip-0: -16px;"><a href="#__code_6_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
<span class="k">def</span><span class="w"> </span><span class="nf">infinite_retry_tool</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
    <span class="k">raise</span> <span class="n">ModelRetry</span><span class="p">(</span><span class="s1">'Please try again.'</span><span class="p">)</span>


<span class="k">try</span><span class="p">:</span>
    <span class="n">result_sync</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span>
        <span class="s1">'Begin infinite retry loop!'</span><span class="p">,</span> <span class="n">usage_limits</span><span class="o">=</span><span class="n">UsageLimits</span><span class="p">(</span><span class="n">request_limit</span><span class="o">=</span><span class="mi">3</span><span class="p">)</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 689px; --md-tooltip-y: 591px; --md-tooltip-0: -16px;"><a href="#__code_6_annotation_2" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="2"></span></a></aside></span>
    <span class="p">)</span>
<span class="k">except</span> <span class="n">UsageLimitExceeded</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">e</span><span class="p">)</span>
    <span class="c1">#&gt; The next request would exceed the request_limit of 3</span>
</code></pre></div>
<ol hidden="">
<li></li>
<li></li>
</ol>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This is especially relevant if you've registered many tools. The <code>request_limit</code> can be used to prevent the model from calling them in a loop too many times.</p>
</div>
<h4 id="model-run-settings">Model (Run) Settings</h4>
<p>PydanticAI offers a <a class="autorefs autorefs-internal" href="../api/settings/#pydantic_ai.settings.ModelSettings"><code>settings.ModelSettings</code></a> structure to help you fine tune your requests.
This structure allows you to configure common parameters that influence the model's behavior, such as <code>temperature</code>, <code>max_tokens</code>,
<code>timeout</code>, and more.</p>
<p>There are two ways to apply these settings:
1. Passing to <code>run{_sync,_stream}</code> functions via the <code>model_settings</code> argument. This allows for fine-tuning on a per-request basis.
2. Setting during <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent"><code>Agent</code></a> initialization via the <code>model_settings</code> argument. These settings will be applied by default to all subsequent run calls using said agent. However, <code>model_settings</code> provided during a specific run call will override the agent's default settings.</p>
<p>For example, if you'd like to set the <code>temperature</code> setting to <code>0.0</code> to ensure less random behavior,
you can do the following:</p>
<div class="language-py highlight"><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'openai:gpt-4o'</span><span class="p">)</span>

<span class="n">result_sync</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span>
    <span class="s1">'What is the capital of Italy?'</span><span class="p">,</span> <span class="n">model_settings</span><span class="o">=</span><span class="p">{</span><span class="s1">'temperature'</span><span class="p">:</span> <span class="mf">0.0</span><span class="p">}</span>
<span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result_sync</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; Rome</span>
</code></pre></div>
<h3 id="model-specific-settings">Model specific settings</h3>
<p>If you wish to further customize model behavior, you can use a subclass of <a class="autorefs autorefs-internal" href="../api/settings/#pydantic_ai.settings.ModelSettings"><code>ModelSettings</code></a>, like <a class="autorefs autorefs-internal" href="../api/models/gemini/#pydantic_ai.models.gemini.GeminiModelSettings"><code>GeminiModelSettings</code></a>, associated with your model of choice.</p>
<p>For example:</p>
<div class="language-py highlight"><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code tabindex="0"><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span><span class="p">,</span> <span class="n">UnexpectedModelBehavior</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.gemini</span><span class="w"> </span><span class="kn">import</span> <span class="n">GeminiModelSettings</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'google-gla:gemini-1.5-flash'</span><span class="p">)</span>

<span class="k">try</span><span class="p">:</span>
    <span class="n">result</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span>
        <span class="s1">'Write a list of 5 very rude things that I might say to the universe after stubbing my toe in the dark:'</span><span class="p">,</span>
        <span class="n">model_settings</span><span class="o">=</span><span class="n">GeminiModelSettings</span><span class="p">(</span>
            <span class="n">temperature</span><span class="o">=</span><span class="mf">0.0</span><span class="p">,</span>  <span class="c1"># general model settings can also be specified</span>
            <span class="n">gemini_safety_settings</span><span class="o">=</span><span class="p">[</span>
                <span class="p">{</span>
                    <span class="s1">'category'</span><span class="p">:</span> <span class="s1">'HARM_CATEGORY_HARASSMENT'</span><span class="p">,</span>
                    <span class="s1">'threshold'</span><span class="p">:</span> <span class="s1">'BLOCK_LOW_AND_ABOVE'</span><span class="p">,</span>
                <span class="p">},</span>
                <span class="p">{</span>
                    <span class="s1">'category'</span><span class="p">:</span> <span class="s1">'HARM_CATEGORY_HATE_SPEECH'</span><span class="p">,</span>
                    <span class="s1">'threshold'</span><span class="p">:</span> <span class="s1">'BLOCK_LOW_AND_ABOVE'</span><span class="p">,</span>
                <span class="p">},</span>
            <span class="p">],</span>
        <span class="p">),</span>
    <span class="p">)</span>
<span class="k">except</span> <span class="n">UnexpectedModelBehavior</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">e</span><span class="p">)</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 142px; --md-tooltip-y: 458px; --md-tooltip-0: -16px;"><a href="#__code_8_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Safety settings triggered, body:</span>
<span class="sd">    &lt;safety settings details&gt;</span>
<span class="sd">    """</span>
</code></pre></div>
<ol hidden="">
<li></li>
</ol>
<h2 id="runs-vs-conversations">Runs vs. Conversations</h2>
<p>An agent <strong>run</strong> might represent an entire conversation — there's no limit to how many messages can be exchanged in a single run. However, a <strong>conversation</strong> might also be composed of multiple runs, especially if you need to maintain state between separate interactions or API calls.</p>
<p>Here's an example of a conversation comprised of multiple runs:</p>
<div class="language-python highlight"><span class="filename">conversation_example.py</span><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'openai:gpt-4o'</span><span class="p">)</span>

<span class="c1"># First run</span>
<span class="n">result1</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'Who was Albert Einstein?'</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result1</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; Albert Einstein was a German-born theoretical physicist.</span>

<span class="c1"># Second run, passing previous messages</span>
<span class="n">result2</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span>
    <span class="s1">'What was his most famous equation?'</span><span class="p">,</span>
<span class="hll">    <span class="n">message_history</span><span class="o">=</span><span class="n">result1</span><span class="o">.</span><span class="n">new_messages</span><span class="p">(),</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 395px; --md-tooltip-y: 249px; --md-tooltip-0: -16px;"><a href="#__code_9_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result2</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; Albert Einstein's most famous equation is (E = mc^2).</span>
</code></pre></div>
<ol hidden="">
<li></li>
</ol>
<p><em>(This example is complete, it can be run "as is")</em></p>
<h2 id="static-type-checking">Type safe by design</h2>
<p>PydanticAI is designed to work well with static type checkers, like mypy and pyright.</p>
<div class="admonition tip">
<p class="admonition-title">Typing is (somewhat) optional</p>
<p>PydanticAI is designed to make type checking as useful as possible for you if you choose to use it, but you don't have to use types everywhere all the time.</p>
<p>That said, because PydanticAI uses Pydantic, and Pydantic uses type hints as the definition for schema and validation, some types (specifically type hints on parameters to tools, and the <code>result_type</code> arguments to <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent"><code>Agent</code></a>) are used at runtime.</p>
<p>We (the library developers) have messed up if type hints are confusing you more than helping you, if you find this, please create an <a href="https://github.com/pydantic/pydantic-ai/issues">issue</a> explaining what's annoying you!</p>
</div>
<p>In particular, agents are generic in both the type of their dependencies and the type of results they return, so you can use the type hints to ensure you're using the right types.</p>
<p>Consider the following script with type mistakes:</p>
<div class="language-python highlight"><span class="filename">type_mistakes.py</span><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">dataclasses</span><span class="w"> </span><span class="kn">import</span> <span class="n">dataclass</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span><span class="p">,</span> <span class="n">RunContext</span>


<span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">User</span><span class="p">:</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>


<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
    <span class="s1">'test'</span><span class="p">,</span>
    <span class="n">deps_type</span><span class="o">=</span><span class="n">User</span><span class="p">,</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 199px; --md-tooltip-y: 249px; --md-tooltip-0: -16px;"><a href="#__code_10_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
    <span class="n">result_type</span><span class="o">=</span><span class="nb">bool</span><span class="p">,</span>
<span class="p">)</span>


<span class="hll"><span class="nd">@agent</span><span class="o">.</span><span class="n">system_prompt</span>
</span><span class="k">def</span><span class="w"> </span><span class="nf">add_user_name</span><span class="p">(</span><span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 428px; --md-tooltip-y: 363px; --md-tooltip-0: -16px;"><a href="#__code_10_annotation_2" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="2"></span></a></aside></span>
    <span class="k">return</span> <span class="sa">f</span><span class="s2">"The user's name is </span><span class="si">{</span><span class="n">ctx</span><span class="o">.</span><span class="n">deps</span><span class="si">}</span><span class="s2">."</span>


<span class="k">def</span><span class="w"> </span><span class="nf">foobar</span><span class="p">(</span><span class="n">x</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
    <span class="k">pass</span>


<span class="n">result</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'Does their name start with "A"?'</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="n">User</span><span class="p">(</span><span class="s1">'Anne'</span><span class="p">))</span>
<span class="hll"><span class="n">foobar</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 199px; --md-tooltip-y: 534px; --md-tooltip-0: -16px;"><a href="#__code_10_annotation_3" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="3"></span></a></aside></span>
</span></code></pre></div>
<ol hidden="">
<li></li>
<li></li>
<li></li>
</ol>
<p>Running <code>mypy</code> on this will give the following output:</p>
<div class="language-bash highlight"><pre id="__code_11"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_11 > code"></button><code tabindex="0">➤<span class="w"> </span>uv<span class="w"> </span>run<span class="w"> </span>mypy<span class="w"> </span>type_mistakes.py
type_mistakes.py:18:<span class="w"> </span>error:<span class="w"> </span>Argument<span class="w"> </span><span class="m">1</span><span class="w"> </span>to<span class="w"> </span><span class="s2">"system_prompt"</span><span class="w"> </span>of<span class="w"> </span><span class="s2">"Agent"</span><span class="w"> </span>has<span class="w"> </span>incompatible<span class="w"> </span><span class="nb">type</span><span class="w"> </span><span class="s2">"Callable[[RunContext[str]], str]"</span><span class="p">;</span><span class="w"> </span>expected<span class="w"> </span><span class="s2">"Callable[[RunContext[User]], str]"</span><span class="w">  </span><span class="o">[</span>arg-type<span class="o">]</span>
type_mistakes.py:28:<span class="w"> </span>error:<span class="w"> </span>Argument<span class="w"> </span><span class="m">1</span><span class="w"> </span>to<span class="w"> </span><span class="s2">"foobar"</span><span class="w"> </span>has<span class="w"> </span>incompatible<span class="w"> </span><span class="nb">type</span><span class="w"> </span><span class="s2">"bool"</span><span class="p">;</span><span class="w"> </span>expected<span class="w"> </span><span class="s2">"bytes"</span><span class="w">  </span><span class="o">[</span>arg-type<span class="o">]</span>
Found<span class="w"> </span><span class="m">2</span><span class="w"> </span>errors<span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="m">1</span><span class="w"> </span>file<span class="w"> </span><span class="o">(</span>checked<span class="w"> </span><span class="m">1</span><span class="w"> </span><span class="nb">source</span><span class="w"> </span>file<span class="o">)</span>
</code></pre></div>
<p>Running <code>pyright</code> would identify the same issues.</p>
<h2 id="system-prompts">System Prompts</h2>
<p>System prompts might seem simple at first glance since they're just strings (or sequences of strings that are concatenated), but crafting the right system prompt is key to getting the model to behave as you want.</p>
<p>Generally, system prompts fall into two categories:</p>
<ol>
<li><strong>Static system prompts</strong>: These are known when writing the code and can be defined via the <code>system_prompt</code> parameter of the <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent.__init__"><code>Agent</code> constructor</a>.</li>
<li><strong>Dynamic system prompts</strong>: These depend in some way on context that isn't known until runtime, and should be defined via functions decorated with <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent.system_prompt"><code>@agent.system_prompt</code></a>.</li>
</ol>
<p>You can add both to a single agent; they're appended in the order they're defined at runtime.</p>
<p>Here's an example using both types of system prompts:</p>
<div class="language-python highlight"><span class="filename">system_prompts.py</span><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">datetime</span><span class="w"> </span><span class="kn">import</span> <span class="n">date</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span><span class="p">,</span> <span class="n">RunContext</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
    <span class="s1">'openai:gpt-4o'</span><span class="p">,</span>
    <span class="n">deps_type</span><span class="o">=</span><span class="nb">str</span><span class="p">,</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 191px; --md-tooltip-y: 134px; --md-tooltip-0: -16px;"><a href="#__code_12_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
    <span class="n">system_prompt</span><span class="o">=</span><span class="s2">"Use the customer's name while replying to them."</span><span class="p">,</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 599px; --md-tooltip-y: 153px; --md-tooltip-0: -16px;"><a href="#__code_12_annotation_2" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="2"></span></a></aside></span>
<span class="p">)</span>


<span class="nd">@agent</span><span class="o">.</span><span class="n">system_prompt</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 208px; --md-tooltip-y: 230px; --md-tooltip-0: -16px;"><a href="#__code_12_annotation_3" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="3"></span></a></aside></span>
<span class="k">def</span><span class="w"> </span><span class="nf">add_the_users_name</span><span class="p">(</span><span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
    <span class="k">return</span> <span class="sa">f</span><span class="s2">"The user's name is </span><span class="si">{</span><span class="n">ctx</span><span class="o">.</span><span class="n">deps</span><span class="si">}</span><span class="s2">."</span>


<span class="nd">@agent</span><span class="o">.</span><span class="n">system_prompt</span>
<span class="k">def</span><span class="w"> </span><span class="nf">add_the_date</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 257px; --md-tooltip-y: 344px; --md-tooltip-0: -16px;"><a href="#__code_12_annotation_4" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="4"></span></a></aside></span>
    <span class="k">return</span> <span class="sa">f</span><span class="s1">'The date is </span><span class="si">{</span><span class="n">date</span><span class="o">.</span><span class="n">today</span><span class="p">()</span><span class="si">}</span><span class="s1">.'</span>


<span class="n">result</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'What is the date?'</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="s1">'Frank'</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; Hello Frank, the date today is 2032-01-02.</span>
</code></pre></div>
<ol hidden="">
<li></li>
<li></li>
<li></li>
<li></li>
</ol>
<p><em>(This example is complete, it can be run "as is")</em></p>
<h2 id="reflection-and-self-correction">Reflection and self-correction</h2>
<p>Validation errors from both function tool parameter validation and <a href="../results/#structured-result-validation">structured result validation</a> can be passed back to the model with a request to retry.</p>
<p>You can also raise <a class="autorefs autorefs-internal" href="../api/exceptions/#pydantic_ai.exceptions.ModelRetry"><code>ModelRetry</code></a> from within a <a href="../tools/">tool</a> or <a href="../results/#result-validators-functions">result validator function</a> to tell the model it should retry generating a response.</p>
<ul>
<li>The default retry count is <strong>1</strong> but can be altered for the <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent.__init__">entire agent</a>, a <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent.tool">specific tool</a>, or a <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent.__init__">result validator</a>.</li>
<li>You can access the current retry count from within a tool or result validator via <a class="autorefs autorefs-internal" href="../api/tools/#pydantic_ai.tools.RunContext"><code>ctx.retry</code></a>.</li>
</ul>
<p>Here's an example:</p>
<div class="language-python highlight"><span class="filename">tool_retry.py</span><pre id="__code_13"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_13 > code"></button><code tabindex="0"><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic</span><span class="w"> </span><span class="kn">import</span> <span class="n">BaseModel</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span><span class="p">,</span> <span class="n">RunContext</span><span class="p">,</span> <span class="n">ModelRetry</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">fake_database</span><span class="w"> </span><span class="kn">import</span> <span class="n">DatabaseConn</span>


<span class="k">class</span><span class="w"> </span><span class="nc">ChatResult</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">user_id</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">message</span><span class="p">:</span> <span class="nb">str</span>


<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
    <span class="s1">'openai:gpt-4o'</span><span class="p">,</span>
    <span class="n">deps_type</span><span class="o">=</span><span class="n">DatabaseConn</span><span class="p">,</span>
    <span class="n">result_type</span><span class="o">=</span><span class="n">ChatResult</span><span class="p">,</span>
<span class="p">)</span>


<span class="nd">@agent</span><span class="o">.</span><span class="n">tool</span><span class="p">(</span><span class="n">retries</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="k">def</span><span class="w"> </span><span class="nf">get_user_by_name</span><span class="p">(</span><span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="n">DatabaseConn</span><span class="p">],</span> <span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get a user's ID from their full name."""</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">name</span><span class="p">)</span>
    <span class="c1">#&gt; John</span>
    <span class="c1">#&gt; John Doe</span>
    <span class="n">user_id</span> <span class="o">=</span> <span class="n">ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">users</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">user_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">ModelRetry</span><span class="p">(</span>
            <span class="sa">f</span><span class="s1">'No user found with name </span><span class="si">{</span><span class="n">name</span><span class="si">!r}</span><span class="s1">, remember to provide their full name'</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="n">user_id</span>


<span class="n">result</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span>
    <span class="s1">'Send a message to John Doe asking for coffee next week'</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="n">DatabaseConn</span><span class="p">()</span>
<span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="sd">"""</span>
<span class="sd">user_id=123 message='Hello John, would you be free for coffee sometime next week? Let me know what works for you!'</span>
<span class="sd">"""</span>
</code></pre></div>
<h2 id="model-errors">Model errors</h2>
<p>If models behave unexpectedly (e.g., the retry limit is exceeded, or their API returns <code>503</code>), agent runs will raise <a class="autorefs autorefs-internal" href="../api/exceptions/#pydantic_ai.exceptions.UnexpectedModelBehavior"><code>UnexpectedModelBehavior</code></a>.</p>
<p>In these cases, <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.capture_run_messages"><code>capture_run_messages</code></a> can be used to access the messages exchanged during the run to help diagnose the issue.</p>
<div class="language-python highlight"><span class="filename">agent_model_errors.py</span><pre id="__code_14"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_14 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span><span class="p">,</span> <span class="n">ModelRetry</span><span class="p">,</span> <span class="n">UnexpectedModelBehavior</span><span class="p">,</span> <span class="n">capture_run_messages</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'openai:gpt-4o'</span><span class="p">)</span>


<span class="nd">@agent</span><span class="o">.</span><span class="n">tool_plain</span>
<span class="k">def</span><span class="w"> </span><span class="nf">calc_volume</span><span class="p">(</span><span class="n">size</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 322px; --md-tooltip-y: 134px; --md-tooltip-0: -16px;"><a href="#__code_14_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
    <span class="k">if</span> <span class="n">size</span> <span class="o">==</span> <span class="mi">42</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">size</span><span class="o">**</span><span class="mi">3</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">ModelRetry</span><span class="p">(</span><span class="s1">'Please try again.'</span><span class="p">)</span>


<span class="k">with</span> <span class="n">capture_run_messages</span><span class="p">()</span> <span class="k">as</span> <span class="n">messages</span><span class="p">:</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 371px; --md-tooltip-y: 268px; --md-tooltip-0: -16px;"><a href="#__code_14_annotation_2" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="2"></span></a></aside></span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'Please get me the volume of a box with size 6.'</span><span class="p">)</span>
    <span class="k">except</span> <span class="n">UnexpectedModelBehavior</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s1">'An error occurred:'</span><span class="p">,</span> <span class="n">e</span><span class="p">)</span>
        <span class="c1">#&gt; An error occurred: Tool exceeded max retries count of 1</span>
        <span class="nb">print</span><span class="p">(</span><span class="s1">'cause:'</span><span class="p">,</span> <span class="nb">repr</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">__cause__</span><span class="p">))</span>
        <span class="c1">#&gt; cause: ModelRetry('Please try again.')</span>
        <span class="nb">print</span><span class="p">(</span><span class="s1">'messages:'</span><span class="p">,</span> <span class="n">messages</span><span class="p">)</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        messages:</span>
<span class="sd">        [</span>
<span class="sd">            ModelRequest(</span>
<span class="sd">                parts=[</span>
<span class="sd">                    UserPromptPart(</span>
<span class="sd">                        content='Please get me the volume of a box with size 6.',</span>
<span class="sd">                        timestamp=datetime.datetime(...),</span>
<span class="sd">                        part_kind='user-prompt',</span>
<span class="sd">                    )</span>
<span class="sd">                ],</span>
<span class="sd">                kind='request',</span>
<span class="sd">            ),</span>
<span class="sd">            ModelResponse(</span>
<span class="sd">                parts=[</span>
<span class="sd">                    ToolCallPart(</span>
<span class="sd">                        tool_name='calc_volume',</span>
<span class="sd">                        args={'size': 6},</span>
<span class="sd">                        tool_call_id='pyd_ai_tool_call_id',</span>
<span class="sd">                        part_kind='tool-call',</span>
<span class="sd">                    )</span>
<span class="sd">                ],</span>
<span class="sd">                model_name='gpt-4o',</span>
<span class="sd">                timestamp=datetime.datetime(...),</span>
<span class="sd">                kind='response',</span>
<span class="sd">            ),</span>
<span class="sd">            ModelRequest(</span>
<span class="sd">                parts=[</span>
<span class="sd">                    RetryPromptPart(</span>
<span class="sd">                        content='Please try again.',</span>
<span class="sd">                        tool_name='calc_volume',</span>
<span class="sd">                        tool_call_id='pyd_ai_tool_call_id',</span>
<span class="sd">                        timestamp=datetime.datetime(...),</span>
<span class="sd">                        part_kind='retry-prompt',</span>
<span class="sd">                    )</span>
<span class="sd">                ],</span>
<span class="sd">                kind='request',</span>
<span class="sd">            ),</span>
<span class="sd">            ModelResponse(</span>
<span class="sd">                parts=[</span>
<span class="sd">                    ToolCallPart(</span>
<span class="sd">                        tool_name='calc_volume',</span>
<span class="sd">                        args={'size': 6},</span>
<span class="sd">                        tool_call_id='pyd_ai_tool_call_id',</span>
<span class="sd">                        part_kind='tool-call',</span>
<span class="sd">                    )</span>
<span class="sd">                ],</span>
<span class="sd">                model_name='gpt-4o',</span>
<span class="sd">                timestamp=datetime.datetime(...),</span>
<span class="sd">                kind='response',</span>
<span class="sd">            ),</span>
<span class="sd">        ]</span>
<span class="sd">        """</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
</code></pre></div>
<ol hidden="">
<li></li>
<li></li>
</ol>
<p><em>(This example is complete, it can be run "as is")</em></p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If you call <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent.run"><code>run</code></a>, <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent.run_sync"><code>run_sync</code></a>, or <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent.run_stream"><code>run_stream</code></a> more than once within a single <code>capture_run_messages</code> context, <code>messages</code> will represent the messages exchanged during the first call only.</p>
</div>







  
  






                
              </article>
            </div>
          
          
  <script>var tabs=__md_get("__tabs");if(Array.isArray(tabs))e:for(var set of document.querySelectorAll(".tabbed-set")){var labels=set.querySelector(".tabbed-labels");for(var tab of tabs)for(var label of labels.getElementsByTagName("label"))if(label.innerText.trim()===tab){var input=document.getElementById(label.htmlFor);input.checked=!0;continue e}}</script>

<script>var target=document.getElementById(location.hash.slice(1));target&&target.name&&(target.checked=target.name.startsWith("__tabbed_"))</script>
        </div>
        
      </main>
      
        <footer class="md-footer">
  
  <div class="md-footer-meta md-typeset">
    <div class="md-footer-meta__inner md-grid">
      <div class="md-copyright">
  
    <div class="md-copyright__highlight">
      © Pydantic Services Inc. 2024 to present
    </div>
  
  
</div>
      
    </div>
  </div>
</footer>
      
    </div>
    <div class="md-dialog" data-md-component="dialog">
      <div class="md-dialog__inner md-typeset"></div>
    </div>
    
    
    <script id="__config" type="application/json">{"base": "..", "features": ["search.suggest", "search.highlight", "content.tabs.link", "content.code.annotate", "content.code.copy", "content.code.select", "navigation.path", "navigation.indexes", "navigation.sections", "navigation.tracking", "toc.follow"], "search": "../assets/javascripts/workers/search.f8cc74c7.min.js", "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}}</script>
    
    
      <script src="../assets/javascripts/bundle.f1b6f286.min.js"></script>
      
        <script src="/flarelytics/client.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/algoliasearch@5.20.0/dist/lite/builds/browser.umd.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4.77.3/dist/instantsearch.production.min.js"></script>
      
        <script src="/javascripts/algolia-search.js"></script>
      
    
  <script id="init-glightbox">const lightbox = GLightbox({"touchNavigation": true, "loop": false, "zoomable": true, "draggable": true, "openEffect": "zoom", "closeEffect": "zoom", "slideEffect": "slide"});
document$.subscribe(() => { lightbox.reload() });
</script>
</body></html>