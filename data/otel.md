<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/api/pydantic_evals/otel/">
      
      
        <link rel="prev" href="../reporting/">
      
      
        <link rel="next" href="../generation/">
      
      
      <link rel="icon" href="../../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>pydantic_evals.otel - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="pydantic_evals.otel - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/api/pydantic_evals/otel.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/api/pydantic_evals/otel/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="pydantic_evals.otel - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/api/pydantic_evals/otel.png">
      
    
    
   <link href="../../../assets/stylesheets/glightbox.min.css" rel="stylesheet"><style>
    html.glightbox-open { overflow: initial; height: 100%; }
    .gslide-title { margin-top: 0px; user-select: text; }
    .gslide-desc { color: #666; user-select: text; }
    .gslide-image img { background: white; }
    .gscrollbar-fixer { padding-right: 15px; }
    .gdesc-inner { font-size: 0.75rem; }
    body[data-md-color-scheme="slate"] .gdesc-inner { background: var(--md-default-bg-color);}
    body[data-md-color-scheme="slate"] .gslide-title { color: var(--md-default-fg-color);}
    body[data-md-color-scheme="slate"] .gslide-desc { color: var(--md-default-fg-color);}</style> <script src="../../../assets/javascripts/glightbox.min.js"></script><meta name="theme-color" content="#e92063"><meta name="color-scheme" content="light"></head>
  
  
    
    
      
    
    
    
    
    <body dir="ltr" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" data-md-color-media="(prefers-color-scheme)">
  
    
    <input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">
    <input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">
    <label class="md-overlay" for="__drawer"></label>
    <div data-md-component="skip">
      
        
        <a href="#pydantic_evalsotel" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
    
      

  

<header class="md-header md-header--shadow" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href="../../.." title="PydanticAI" class="md-header__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../../img/logo-white.svg" alt="logo">

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
            
              pydantic_evals.otel
            
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
    <a href="../../.." title="PydanticAI" class="md-nav__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../../img/logo-white.svg" alt="logo">

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
      <a href="../../.." class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Introduction
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../install/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Installation
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../help/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Getting Help
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../contributing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Contributing
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../troubleshooting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Troubleshooting
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6">
        
          
          <label class="md-nav__link" for="__nav_6" id="__nav_6_label" tabindex="">
            
  
  <span class="md-ellipsis">
    Documentation
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_6_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_6">
            <span class="md-nav__icon md-icon"></span>
            Documentation
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../agents/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../models/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../dependencies/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Dependencies
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Function Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../common-tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Common Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../results/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Results
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../message-history/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Messages and chat history
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../testing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Unit testing
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../logfire/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Debugging and Monitoring
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../multi-agent-applications/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Multi-agent Applications
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Graphs
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../evals/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Evals
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../input/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Image, Audio &amp; Document Input
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_14">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../../../mcp/" class="md-nav__link ">
              
  
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
      <a href="../../../mcp/client/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Client
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../mcp/server/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Server
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../mcp/run-python/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    MCP Run Python
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../cli/" class="md-nav__link">
        
  
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
            <a href="../../../examples/" class="md-nav__link ">
              
  
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
      <a href="../../../examples/pydantic-model/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Pydantic Model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/weather-agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Weather agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/bank-support/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Bank support
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/sql-gen/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    SQL Generation
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/flight-booking/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Flight booking
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/rag/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    RAG
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/stream-markdown/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream markdown
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/stream-whales/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream whales
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/chat-app/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Chat App with FastAPI
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/question-graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Question Graph
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
    
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_8" checked="">
        
          
          <label class="md-nav__link" for="__nav_8" id="__nav_8_label" tabindex="">
            
  
  <span class="md-ellipsis">
    API Reference
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_8_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_8">
            <span class="md-nav__icon md-icon"></span>
            API Reference
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../common_tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.common_tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../result/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../messages/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../settings/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.settings
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../usage/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.usage
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../mcp/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.mcp
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../format_as_xml/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.format_as_xml
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/base/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/openai/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.openai
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/anthropic/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.anthropic
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/bedrock/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.bedrock
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/cohere/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.cohere
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/gemini/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.gemini
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/groq/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.groq
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/instrumented/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/mistral/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.test
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/function/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/fallback/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/wrapper/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.wrapper
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../providers/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.providers
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/nodes/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.nodes
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/persistence/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/mermaid/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../dataset/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../evaluators/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.otel" class="md-nav__link">
    <span class="md-ellipsis">
      otel
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode" class="md-nav__link">
    <span class="md-ellipsis">
      SpanNode
    </span>
  </a>
  
    <nav class="md-nav" aria-label="SpanNode">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.duration" class="md-nav__link">
    <span class="md-ellipsis">
      duration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.descendants" class="md-nav__link">
    <span class="md-ellipsis">
      descendants
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.ancestors" class="md-nav__link">
    <span class="md-ellipsis">
      ancestors
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.add_child" class="md-nav__link">
    <span class="md-ellipsis">
      add_child
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.find_children" class="md-nav__link">
    <span class="md-ellipsis">
      find_children
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.first_child" class="md-nav__link">
    <span class="md-ellipsis">
      first_child
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.any_child" class="md-nav__link">
    <span class="md-ellipsis">
      any_child
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.find_descendants" class="md-nav__link">
    <span class="md-ellipsis">
      find_descendants
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.first_descendant" class="md-nav__link">
    <span class="md-ellipsis">
      first_descendant
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.any_descendant" class="md-nav__link">
    <span class="md-ellipsis">
      any_descendant
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.find_ancestors" class="md-nav__link">
    <span class="md-ellipsis">
      find_ancestors
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.first_ancestor" class="md-nav__link">
    <span class="md-ellipsis">
      first_ancestor
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.any_ancestor" class="md-nav__link">
    <span class="md-ellipsis">
      any_ancestor
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.matches" class="md-nav__link">
    <span class="md-ellipsis">
      matches
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.repr_xml" class="md-nav__link">
    <span class="md-ellipsis">
      repr_xml
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanQuery" class="md-nav__link">
    <span class="md-ellipsis">
      SpanQuery
    </span>
  </a>
  
    <nav class="md-nav" aria-label="SpanQuery">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanQuery.stop_recursing_when" class="md-nav__link">
    <span class="md-ellipsis">
      stop_recursing_when
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanTree" class="md-nav__link">
    <span class="md-ellipsis">
      SpanTree
    </span>
  </a>
  
    <nav class="md-nav" aria-label="SpanTree">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanTree.add_spans" class="md-nav__link">
    <span class="md-ellipsis">
      add_spans
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanTree.find" class="md-nav__link">
    <span class="md-ellipsis">
      find
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanTree.first" class="md-nav__link">
    <span class="md-ellipsis">
      first
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanTree.any" class="md-nav__link">
    <span class="md-ellipsis">
      any
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanTree.__iter__" class="md-nav__link">
    <span class="md-ellipsis">
      __iter__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanTree.repr_xml" class="md-nav__link">
    <span class="md-ellipsis">
      repr_xml
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../generation/" class="md-nav__link">
        
  
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
  <a href="#pydantic_evals.otel" class="md-nav__link">
    <span class="md-ellipsis">
      otel
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode" class="md-nav__link">
    <span class="md-ellipsis">
      SpanNode
    </span>
  </a>
  
    <nav class="md-nav" aria-label="SpanNode">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.duration" class="md-nav__link">
    <span class="md-ellipsis">
      duration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.descendants" class="md-nav__link">
    <span class="md-ellipsis">
      descendants
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.ancestors" class="md-nav__link">
    <span class="md-ellipsis">
      ancestors
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.add_child" class="md-nav__link">
    <span class="md-ellipsis">
      add_child
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.find_children" class="md-nav__link">
    <span class="md-ellipsis">
      find_children
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.first_child" class="md-nav__link">
    <span class="md-ellipsis">
      first_child
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.any_child" class="md-nav__link">
    <span class="md-ellipsis">
      any_child
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.find_descendants" class="md-nav__link">
    <span class="md-ellipsis">
      find_descendants
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.first_descendant" class="md-nav__link">
    <span class="md-ellipsis">
      first_descendant
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.any_descendant" class="md-nav__link">
    <span class="md-ellipsis">
      any_descendant
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.find_ancestors" class="md-nav__link">
    <span class="md-ellipsis">
      find_ancestors
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.first_ancestor" class="md-nav__link">
    <span class="md-ellipsis">
      first_ancestor
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.any_ancestor" class="md-nav__link">
    <span class="md-ellipsis">
      any_ancestor
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.matches" class="md-nav__link">
    <span class="md-ellipsis">
      matches
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanNode.repr_xml" class="md-nav__link">
    <span class="md-ellipsis">
      repr_xml
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanQuery" class="md-nav__link">
    <span class="md-ellipsis">
      SpanQuery
    </span>
  </a>
  
    <nav class="md-nav" aria-label="SpanQuery">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanQuery.stop_recursing_when" class="md-nav__link">
    <span class="md-ellipsis">
      stop_recursing_when
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanTree" class="md-nav__link">
    <span class="md-ellipsis">
      SpanTree
    </span>
  </a>
  
    <nav class="md-nav" aria-label="SpanTree">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanTree.add_spans" class="md-nav__link">
    <span class="md-ellipsis">
      add_spans
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanTree.find" class="md-nav__link">
    <span class="md-ellipsis">
      find
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanTree.first" class="md-nav__link">
    <span class="md-ellipsis">
      first
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanTree.any" class="md-nav__link">
    <span class="md-ellipsis">
      any
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanTree.__iter__" class="md-nav__link">
    <span class="md-ellipsis">
      __iter__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.otel.SpanTree.repr_xml" class="md-nav__link">
    <span class="md-ellipsis">
      repr_xml
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
            
          
          
            <div class="md-content" data-md-component="content">
              <article class="md-content__inner md-typeset">
                
                  


  
  


<h1 id="pydantic_evalsotel"><code>pydantic_evals.otel</code></h1>


<div class="doc doc-object doc-module">



<a id="pydantic_evals.otel"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">























<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.otel.SpanNode" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">SpanNode</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>A node in the span tree; provides references to parents/children for easy traversal and queries.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span>
<span class="normal">377</span>
<span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span>
<span class="normal">382</span>
<span class="normal">383</span>
<span class="normal">384</span>
<span class="normal">385</span>
<span class="normal">386</span>
<span class="normal">387</span>
<span class="normal">388</span>
<span class="normal">389</span>
<span class="normal">390</span>
<span class="normal">391</span>
<span class="normal">392</span>
<span class="normal">393</span>
<span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span>
<span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span>
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span>
<span class="normal">417</span>
<span class="normal">418</span>
<span class="normal">419</span>
<span class="normal">420</span>
<span class="normal">421</span>
<span class="normal">422</span>
<span class="normal">423</span>
<span class="normal">424</span>
<span class="normal">425</span>
<span class="normal">426</span>
<span class="normal">427</span>
<span class="normal">428</span>
<span class="normal">429</span>
<span class="normal">430</span>
<span class="normal">431</span>
<span class="normal">432</span></pre></div></td><td class="code"><div><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code tabindex="0"><span class="nd">@dataclass</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="k">class</span><span class="w"> </span><span class="nc">SpanNode</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""A node in the span tree; provides references to parents/children for easy traversal and queries."""</span>

    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">trace_id</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">span_id</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">parent_span_id</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="n">start_timestamp</span><span class="p">:</span> <span class="n">datetime</span>
    <span class="n">end_timestamp</span><span class="p">:</span> <span class="n">datetime</span>
    <span class="n">attributes</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">AttributeValue</span><span class="p">]</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">duration</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">timedelta</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return the span's duration as a timedelta, or None if start/end not set."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">end_timestamp</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">start_timestamp</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">children</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">]:</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">children_by_id</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">descendants</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Return all descendants of this node in DFS order."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">find_descendants</span><span class="p">(</span><span class="k">lambda</span> <span class="n">_</span><span class="p">:</span> <span class="kc">True</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">ancestors</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Return all ancestors of this node."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">find_ancestors</span><span class="p">(</span><span class="k">lambda</span> <span class="n">_</span><span class="p">:</span> <span class="kc">True</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">node_key</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">trace_id</span><span class="si">:</span><span class="s1">032x</span><span class="si">}</span><span class="s1">:</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">span_id</span><span class="si">:</span><span class="s1">016x</span><span class="si">}</span><span class="s1">'</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">parent_node_key</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">parent_span_id</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">trace_id</span><span class="si">:</span><span class="s1">032x</span><span class="si">}</span><span class="s1">:</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">parent_span_id</span><span class="si">:</span><span class="s1">016x</span><span class="si">}</span><span class="s1">'</span>

    <span class="c1"># -------------------------------------------------------------------------</span>
    <span class="c1"># Construction</span>
    <span class="c1"># -------------------------------------------------------------------------</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">__post_init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">parent</span><span class="p">:</span> <span class="n">SpanNode</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">children_by_id</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">SpanNode</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">from_readable_span</span><span class="p">(</span><span class="n">span</span><span class="p">:</span> <span class="n">ReadableSpan</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SpanNode</span><span class="p">:</span>
        <span class="k">assert</span> <span class="n">span</span><span class="o">.</span><span class="n">context</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Span has no context'</span>
        <span class="k">assert</span> <span class="n">span</span><span class="o">.</span><span class="n">start_time</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Span has no start time'</span>
        <span class="k">assert</span> <span class="n">span</span><span class="o">.</span><span class="n">end_time</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Span has no end time'</span>
        <span class="k">return</span> <span class="n">SpanNode</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="n">span</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
            <span class="n">trace_id</span><span class="o">=</span><span class="n">span</span><span class="o">.</span><span class="n">context</span><span class="o">.</span><span class="n">trace_id</span><span class="p">,</span>
            <span class="n">span_id</span><span class="o">=</span><span class="n">span</span><span class="o">.</span><span class="n">context</span><span class="o">.</span><span class="n">span_id</span><span class="p">,</span>
            <span class="n">parent_span_id</span><span class="o">=</span><span class="n">span</span><span class="o">.</span><span class="n">parent</span><span class="o">.</span><span class="n">span_id</span> <span class="k">if</span> <span class="n">span</span><span class="o">.</span><span class="n">parent</span> <span class="k">else</span> <span class="kc">None</span><span class="p">,</span>
            <span class="n">start_timestamp</span><span class="o">=</span><span class="n">datetime</span><span class="o">.</span><span class="n">fromtimestamp</span><span class="p">(</span><span class="n">span</span><span class="o">.</span><span class="n">start_time</span> <span class="o">/</span> <span class="mf">1e9</span><span class="p">,</span> <span class="n">tz</span><span class="o">=</span><span class="n">timezone</span><span class="o">.</span><span class="n">utc</span><span class="p">),</span>
            <span class="n">end_timestamp</span><span class="o">=</span><span class="n">datetime</span><span class="o">.</span><span class="n">fromtimestamp</span><span class="p">(</span><span class="n">span</span><span class="o">.</span><span class="n">end_time</span> <span class="o">/</span> <span class="mf">1e9</span><span class="p">,</span> <span class="n">tz</span><span class="o">=</span><span class="n">timezone</span><span class="o">.</span><span class="n">utc</span><span class="p">),</span>
            <span class="n">attributes</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">span</span><span class="o">.</span><span class="n">attributes</span> <span class="ow">or</span> <span class="p">{}),</span>
        <span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">add_child</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">child</span><span class="p">:</span> <span class="n">SpanNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Attach a child node to this node's list of children."""</span>
        <span class="k">assert</span> <span class="n">child</span><span class="o">.</span><span class="n">trace_id</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">trace_id</span><span class="p">,</span> <span class="sa">f</span><span class="s2">"traces don't match: </span><span class="si">{</span><span class="n">child</span><span class="o">.</span><span class="n">trace_id</span><span class="si">:</span><span class="s2">032x</span><span class="si">}</span><span class="s2"> != </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">trace_id</span><span class="si">:</span><span class="s2">032x</span><span class="si">}</span><span class="s2">"</span>
        <span class="k">assert</span> <span class="n">child</span><span class="o">.</span><span class="n">parent_span_id</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">span_id</span><span class="p">,</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s1">'parent span mismatch: </span><span class="si">{</span><span class="n">child</span><span class="o">.</span><span class="n">parent_span_id</span><span class="si">:</span><span class="s1">016x</span><span class="si">}</span><span class="s1"> != </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">span_id</span><span class="si">:</span><span class="s1">016x</span><span class="si">}</span><span class="s1">'</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">children_by_id</span><span class="p">[</span><span class="n">child</span><span class="o">.</span><span class="n">node_key</span><span class="p">]</span> <span class="o">=</span> <span class="n">child</span>
        <span class="n">child</span><span class="o">.</span><span class="n">parent</span> <span class="o">=</span> <span class="bp">self</span>

    <span class="c1"># -------------------------------------------------------------------------</span>
    <span class="c1"># Child queries</span>
    <span class="c1"># -------------------------------------------------------------------------</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">find_children</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Return all immediate children that satisfy the given predicate."""</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_filter_children</span><span class="p">(</span><span class="n">predicate</span><span class="p">))</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">first_child</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SpanNode</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return the first immediate child that satisfies the given predicate, or None if none match."""</span>
        <span class="k">return</span> <span class="nb">next</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_filter_children</span><span class="p">(</span><span class="n">predicate</span><span class="p">),</span> <span class="kc">None</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">any_child</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Returns True if there is at least one child that satisfies the predicate."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">first_child</span><span class="p">(</span><span class="n">predicate</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_filter_children</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterator</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">]:</span>
        <span class="k">return</span> <span class="p">(</span><span class="n">child</span> <span class="k">for</span> <span class="n">child</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">children</span> <span class="k">if</span> <span class="n">child</span><span class="o">.</span><span class="n">matches</span><span class="p">(</span><span class="n">predicate</span><span class="p">))</span>

    <span class="c1"># -------------------------------------------------------------------------</span>
    <span class="c1"># Descendant queries (DFS)</span>
    <span class="c1"># -------------------------------------------------------------------------</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">find_descendants</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Return all descendant nodes that satisfy the given predicate in DFS order."""</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_filter_descendants</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">))</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">first_descendant</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SpanNode</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""DFS: Return the first descendant (in DFS order) that satisfies the given predicate, or `None` if none match."""</span>
        <span class="k">return</span> <span class="nb">next</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_filter_descendants</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">),</span> <span class="kc">None</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">any_descendant</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Returns `True` if there is at least one descendant that satisfies the predicate."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">first_descendant</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_filter_descendants</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterator</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">]:</span>
        <span class="n">stack</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">)</span>
        <span class="k">while</span> <span class="n">stack</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">stack</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">matches</span><span class="p">(</span><span class="n">predicate</span><span class="p">):</span>
                <span class="k">yield</span> <span class="n">node</span>
            <span class="k">if</span> <span class="n">stop_recursing_when</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">node</span><span class="o">.</span><span class="n">matches</span><span class="p">(</span><span class="n">stop_recursing_when</span><span class="p">):</span>
                <span class="k">continue</span>
            <span class="n">stack</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">children</span><span class="p">)</span>

    <span class="c1"># -------------------------------------------------------------------------</span>
    <span class="c1"># Ancestor queries (DFS "up" the chain)</span>
    <span class="c1"># -------------------------------------------------------------------------</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">find_ancestors</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Return all ancestors that satisfy the given predicate."""</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_filter_ancestors</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">))</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">first_ancestor</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SpanNode</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return the closest ancestor that satisfies the given predicate, or `None` if none match."""</span>
        <span class="k">return</span> <span class="nb">next</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_filter_ancestors</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">),</span> <span class="kc">None</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">any_ancestor</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Returns True if any ancestor satisfies the predicate."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">first_ancestor</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_filter_ancestors</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterator</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">]:</span>
        <span class="n">node</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parent</span>
        <span class="k">while</span> <span class="n">node</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">matches</span><span class="p">(</span><span class="n">predicate</span><span class="p">):</span>
                <span class="k">yield</span> <span class="n">node</span>
            <span class="k">if</span> <span class="n">stop_recursing_when</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">node</span><span class="o">.</span><span class="n">matches</span><span class="p">(</span><span class="n">stop_recursing_when</span><span class="p">):</span>
                <span class="k">break</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">parent</span>

    <span class="c1"># -------------------------------------------------------------------------</span>
    <span class="c1"># Query matching</span>
    <span class="c1"># -------------------------------------------------------------------------</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">matches</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Check if the span node matches the query conditions or predicate."""</span>
        <span class="k">if</span> <span class="nb">callable</span><span class="p">(</span><span class="n">query</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">query</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_matches_query</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_matches_query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">SpanQuery</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>  <span class="c1"># noqa C901</span>
<span class="w">        </span><span class="sd">"""Check if the span matches the query conditions."""</span>
        <span class="c1"># Logical combinations</span>
        <span class="k">if</span> <span class="n">or_</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'or_'</span><span class="p">):</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">query</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Cannot combine 'or_' conditions with other conditions at the same level"</span><span class="p">)</span>
            <span class="k">return</span> <span class="nb">any</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_matches_query</span><span class="p">(</span><span class="n">q</span><span class="p">)</span> <span class="k">for</span> <span class="n">q</span> <span class="ow">in</span> <span class="n">or_</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">not_</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'not_'</span><span class="p">):</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_matches_query</span><span class="p">(</span><span class="n">not_</span><span class="p">):</span>
                <span class="k">return</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="n">and_</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'and_'</span><span class="p">):</span>
            <span class="n">results</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_matches_query</span><span class="p">(</span><span class="n">q</span><span class="p">)</span> <span class="k">for</span> <span class="n">q</span> <span class="ow">in</span> <span class="n">and_</span><span class="p">]</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="nb">all</span><span class="p">(</span><span class="n">results</span><span class="p">):</span>
                <span class="k">return</span> <span class="kc">False</span>
        <span class="c1"># At this point, all existing ANDs and no existing ORs have passed, so it comes down to this condition</span>

        <span class="c1"># Name conditions</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">name_equals</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'name_equals'</span><span class="p">))</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">!=</span> <span class="n">name_equals</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">name_contains</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'name_contains'</span><span class="p">))</span> <span class="ow">and</span> <span class="n">name_contains</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">name_matches_regex</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'name_matches_regex'</span><span class="p">))</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">name_matches_regex</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">):</span>
            <span class="k">return</span> <span class="kc">False</span>

        <span class="c1"># Attribute conditions</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">has_attributes</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'has_attributes'</span><span class="p">))</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">all</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">attributes</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">key</span><span class="p">)</span> <span class="o">==</span> <span class="n">value</span> <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">has_attributes</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
        <span class="p">):</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">has_attributes_keys</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'has_attribute_keys'</span><span class="p">))</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">all</span><span class="p">(</span>
            <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">attributes</span> <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">has_attributes_keys</span>
        <span class="p">):</span>
            <span class="k">return</span> <span class="kc">False</span>

        <span class="c1"># Timing conditions</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">min_duration</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'min_duration'</span><span class="p">))</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">min_duration</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span>
                <span class="n">min_duration</span> <span class="o">=</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">seconds</span><span class="o">=</span><span class="n">min_duration</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">duration</span> <span class="o">&lt;</span> <span class="n">min_duration</span><span class="p">:</span>
                <span class="k">return</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">max_duration</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'max_duration'</span><span class="p">))</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">max_duration</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span>
                <span class="n">max_duration</span> <span class="o">=</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">seconds</span><span class="o">=</span><span class="n">max_duration</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">duration</span> <span class="o">&gt;</span> <span class="n">max_duration</span><span class="p">:</span>
                <span class="k">return</span> <span class="kc">False</span>

        <span class="c1"># Children conditions</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">min_child_count</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'min_child_count'</span><span class="p">))</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">)</span> <span class="o">&lt;</span> <span class="n">min_child_count</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">max_child_count</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'max_child_count'</span><span class="p">))</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">)</span> <span class="o">&gt;</span> <span class="n">max_child_count</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">some_child_has</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'some_child_has'</span><span class="p">))</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">any</span><span class="p">(</span>
            <span class="n">child</span><span class="o">.</span><span class="n">_matches_query</span><span class="p">(</span><span class="n">some_child_has</span><span class="p">)</span> <span class="k">for</span> <span class="n">child</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">children</span>
        <span class="p">):</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">all_children_have</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'all_children_have'</span><span class="p">))</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">all</span><span class="p">(</span>
            <span class="n">child</span><span class="o">.</span><span class="n">_matches_query</span><span class="p">(</span><span class="n">all_children_have</span><span class="p">)</span> <span class="k">for</span> <span class="n">child</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">children</span>
        <span class="p">):</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">no_child_has</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'no_child_has'</span><span class="p">))</span> <span class="ow">and</span> <span class="nb">any</span><span class="p">(</span>
            <span class="n">child</span><span class="o">.</span><span class="n">_matches_query</span><span class="p">(</span><span class="n">no_child_has</span><span class="p">)</span> <span class="k">for</span> <span class="n">child</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">children</span>
        <span class="p">):</span>
            <span class="k">return</span> <span class="kc">False</span>

        <span class="c1"># Descendant conditions</span>
        <span class="c1"># The following local functions with cache decorators are used to avoid repeatedly evaluating these properties</span>
        <span class="nd">@cache</span>
        <span class="k">def</span><span class="w"> </span><span class="nf">descendants</span><span class="p">():</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">descendants</span>

        <span class="nd">@cache</span>
        <span class="k">def</span><span class="w"> </span><span class="nf">pruned_descendants</span><span class="p">():</span>
            <span class="n">stop_recursing_when</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'stop_recursing_when'</span><span class="p">)</span>
            <span class="k">return</span> <span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_filter_descendants</span><span class="p">(</span><span class="k">lambda</span> <span class="n">_</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">)</span> <span class="k">if</span> <span class="n">stop_recursing_when</span> <span class="k">else</span> <span class="n">descendants</span><span class="p">()</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="p">(</span><span class="n">min_descendant_count</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'min_descendant_count'</span><span class="p">))</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">descendants</span><span class="p">())</span> <span class="o">&lt;</span> <span class="n">min_descendant_count</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">max_descendant_count</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'max_descendant_count'</span><span class="p">))</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">descendants</span><span class="p">())</span> <span class="o">&gt;</span> <span class="n">max_descendant_count</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">some_descendant_has</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'some_descendant_has'</span><span class="p">))</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">any</span><span class="p">(</span>
            <span class="n">descendant</span><span class="o">.</span><span class="n">_matches_query</span><span class="p">(</span><span class="n">some_descendant_has</span><span class="p">)</span> <span class="k">for</span> <span class="n">descendant</span> <span class="ow">in</span> <span class="n">pruned_descendants</span><span class="p">()</span>
        <span class="p">):</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">all_descendants_have</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'all_descendants_have'</span><span class="p">))</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">all</span><span class="p">(</span>
            <span class="n">descendant</span><span class="o">.</span><span class="n">_matches_query</span><span class="p">(</span><span class="n">all_descendants_have</span><span class="p">)</span> <span class="k">for</span> <span class="n">descendant</span> <span class="ow">in</span> <span class="n">pruned_descendants</span><span class="p">()</span>
        <span class="p">):</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">no_descendant_has</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'no_descendant_has'</span><span class="p">))</span> <span class="ow">and</span> <span class="nb">any</span><span class="p">(</span>
            <span class="n">descendant</span><span class="o">.</span><span class="n">_matches_query</span><span class="p">(</span><span class="n">no_descendant_has</span><span class="p">)</span> <span class="k">for</span> <span class="n">descendant</span> <span class="ow">in</span> <span class="n">pruned_descendants</span><span class="p">()</span>
        <span class="p">):</span>
            <span class="k">return</span> <span class="kc">False</span>

        <span class="c1"># Ancestor conditions</span>
        <span class="c1"># The following local functions with cache decorators are used to avoid repeatedly evaluating these properties</span>
        <span class="nd">@cache</span>
        <span class="k">def</span><span class="w"> </span><span class="nf">ancestors</span><span class="p">():</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">ancestors</span>

        <span class="nd">@cache</span>
        <span class="k">def</span><span class="w"> </span><span class="nf">pruned_ancestors</span><span class="p">():</span>
            <span class="n">stop_recursing_when</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'stop_recursing_when'</span><span class="p">)</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_filter_ancestors</span><span class="p">(</span><span class="k">lambda</span> <span class="n">_</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">)</span> <span class="k">if</span> <span class="n">stop_recursing_when</span> <span class="k">else</span> <span class="n">ancestors</span><span class="p">()</span>

        <span class="k">if</span> <span class="p">(</span><span class="n">min_depth</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'min_depth'</span><span class="p">))</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">ancestors</span><span class="p">())</span> <span class="o">&lt;</span> <span class="n">min_depth</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">max_depth</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'max_depth'</span><span class="p">))</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">ancestors</span><span class="p">())</span> <span class="o">&gt;</span> <span class="n">max_depth</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">some_ancestor_has</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'some_ancestor_has'</span><span class="p">))</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">any</span><span class="p">(</span>
            <span class="n">ancestor</span><span class="o">.</span><span class="n">_matches_query</span><span class="p">(</span><span class="n">some_ancestor_has</span><span class="p">)</span> <span class="k">for</span> <span class="n">ancestor</span> <span class="ow">in</span> <span class="n">pruned_ancestors</span><span class="p">()</span>
        <span class="p">):</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">all_ancestors_have</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'all_ancestors_have'</span><span class="p">))</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">all</span><span class="p">(</span>
            <span class="n">ancestor</span><span class="o">.</span><span class="n">_matches_query</span><span class="p">(</span><span class="n">all_ancestors_have</span><span class="p">)</span> <span class="k">for</span> <span class="n">ancestor</span> <span class="ow">in</span> <span class="n">pruned_ancestors</span><span class="p">()</span>
        <span class="p">):</span>
            <span class="k">return</span> <span class="kc">False</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">no_ancestor_has</span> <span class="o">:=</span> <span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'no_ancestor_has'</span><span class="p">))</span> <span class="ow">and</span> <span class="nb">any</span><span class="p">(</span>
            <span class="n">ancestor</span><span class="o">.</span><span class="n">_matches_query</span><span class="p">(</span><span class="n">no_ancestor_has</span><span class="p">)</span> <span class="k">for</span> <span class="n">ancestor</span> <span class="ow">in</span> <span class="n">pruned_ancestors</span><span class="p">()</span>
        <span class="p">):</span>
            <span class="k">return</span> <span class="kc">False</span>

        <span class="k">return</span> <span class="kc">True</span>

    <span class="c1"># -------------------------------------------------------------------------</span>
    <span class="c1"># String representation</span>
    <span class="c1"># -------------------------------------------------------------------------</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">repr_xml</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">include_children</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">include_trace_id</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">include_span_id</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">include_start_timestamp</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">include_duration</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return an XML-like string representation of the node.</span>

<span class="sd">        Optionally includes children, trace_id, span_id, start_timestamp, and duration.</span>
<span class="sd">        """</span>
        <span class="n">first_line_parts</span> <span class="o">=</span> <span class="p">[</span><span class="sa">f</span><span class="s1">'&lt;SpanNode name=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">!r}</span><span class="s1">'</span><span class="p">]</span>
        <span class="k">if</span> <span class="n">include_trace_id</span><span class="p">:</span>
            <span class="n">first_line_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"trace_id='</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">trace_id</span><span class="si">:</span><span class="s2">032x</span><span class="si">}</span><span class="s2">'"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">include_span_id</span><span class="p">:</span>
            <span class="n">first_line_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"span_id='</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">span_id</span><span class="si">:</span><span class="s2">016x</span><span class="si">}</span><span class="s2">'"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">include_start_timestamp</span><span class="p">:</span>
            <span class="n">first_line_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">'start_timestamp=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">start_timestamp</span><span class="o">.</span><span class="n">isoformat</span><span class="p">()</span><span class="si">!r}</span><span class="s1">'</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">include_duration</span><span class="p">:</span>
            <span class="n">first_line_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"duration='</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">duration</span><span class="si">}</span><span class="s2">'"</span><span class="p">)</span>

        <span class="n">extra_lines</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="n">include_children</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">:</span>
            <span class="n">first_line_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">'&gt;'</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">child</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">:</span>
                <span class="n">extra_lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">indent</span><span class="p">(</span>
                        <span class="n">child</span><span class="o">.</span><span class="n">repr_xml</span><span class="p">(</span>
                            <span class="n">include_children</span><span class="o">=</span><span class="n">include_children</span><span class="p">,</span>
                            <span class="n">include_trace_id</span><span class="o">=</span><span class="n">include_trace_id</span><span class="p">,</span>
                            <span class="n">include_span_id</span><span class="o">=</span><span class="n">include_span_id</span><span class="p">,</span>
                            <span class="n">include_start_timestamp</span><span class="o">=</span><span class="n">include_start_timestamp</span><span class="p">,</span>
                            <span class="n">include_duration</span><span class="o">=</span><span class="n">include_duration</span><span class="p">,</span>
                        <span class="p">),</span>
                        <span class="s1">'  '</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">)</span>
            <span class="n">extra_lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">'&lt;/SpanNode&gt;'</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">:</span>
                <span class="n">first_line_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">'children=...'</span><span class="p">)</span>
            <span class="n">first_line_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">'/&gt;'</span><span class="p">)</span>
        <span class="k">return</span> <span class="s1">'</span><span class="se">\n</span><span class="s1">'</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="s1">' '</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">first_line_parts</span><span class="p">),</span> <span class="o">*</span><span class="n">extra_lines</span><span class="p">])</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">:</span>
            <span class="k">return</span> <span class="sa">f</span><span class="s2">"&lt;SpanNode name=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">!r}</span><span class="s2"> span_id='</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">span_id</span><span class="si">:</span><span class="s2">016x</span><span class="si">}</span><span class="s2">'&gt;...&lt;/SpanNode&gt;"</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="sa">f</span><span class="s2">"&lt;SpanNode name=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">!r}</span><span class="s2"> span_id='</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">span_id</span><span class="si">:</span><span class="s2">016x</span><span class="si">}</span><span class="s2">' /&gt;"</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">repr_xml</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.otel.SpanNode.duration" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">duration</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code><span class="n">duration</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="datetime.timedelta" href="https://docs.python.org/3/library/datetime.html#datetime.timedelta">timedelta</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return the span's duration as a timedelta, or None if start/end not set.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.otel.SpanNode.descendants" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">descendants</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="n">descendants</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanNode" href="#pydantic_evals.otel.SpanNode">SpanNode</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return all descendants of this node in DFS order.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.otel.SpanNode.ancestors" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">ancestors</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code><span class="n">ancestors</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanNode" href="#pydantic_evals.otel.SpanNode">SpanNode</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return all ancestors of this node.</p>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.otel.SpanNode.add_child" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">add_child</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code><span class="nf">add_child</span><span class="p">(</span><span class="n">child</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanNode" href="#pydantic_evals.otel.SpanNode">SpanNode</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Attach a child node to this node's list of children.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span></pre></div></td><td class="code"><div><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">add_child</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">child</span><span class="p">:</span> <span class="n">SpanNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Attach a child node to this node's list of children."""</span>
    <span class="k">assert</span> <span class="n">child</span><span class="o">.</span><span class="n">trace_id</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">trace_id</span><span class="p">,</span> <span class="sa">f</span><span class="s2">"traces don't match: </span><span class="si">{</span><span class="n">child</span><span class="o">.</span><span class="n">trace_id</span><span class="si">:</span><span class="s2">032x</span><span class="si">}</span><span class="s2"> != </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">trace_id</span><span class="si">:</span><span class="s2">032x</span><span class="si">}</span><span class="s2">"</span>
    <span class="k">assert</span> <span class="n">child</span><span class="o">.</span><span class="n">parent_span_id</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">span_id</span><span class="p">,</span> <span class="p">(</span>
        <span class="sa">f</span><span class="s1">'parent span mismatch: </span><span class="si">{</span><span class="n">child</span><span class="o">.</span><span class="n">parent_span_id</span><span class="si">:</span><span class="s1">016x</span><span class="si">}</span><span class="s1"> != </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">span_id</span><span class="si">:</span><span class="s1">016x</span><span class="si">}</span><span class="s1">'</span>
    <span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">children_by_id</span><span class="p">[</span><span class="n">child</span><span class="o">.</span><span class="n">node_key</span><span class="p">]</span> <span class="o">=</span> <span class="n">child</span>
    <span class="n">child</span><span class="o">.</span><span class="n">parent</span> <span class="o">=</span> <span class="bp">self</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.otel.SpanNode.find_children" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">find_children</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code><span class="nf">find_children</span><span class="p">(</span>
    <span class="n">predicate</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanNode" href="#pydantic_evals.otel.SpanNode">SpanNode</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return all immediate children that satisfy the given predicate.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span></pre></div></td><td class="code"><div><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">find_children</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Return all immediate children that satisfy the given predicate."""</span>
    <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_filter_children</span><span class="p">(</span><span class="n">predicate</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.otel.SpanNode.first_child" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">first_child</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code><span class="nf">first_child</span><span class="p">(</span>
    <span class="n">predicate</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanNode" href="#pydantic_evals.otel.SpanNode">SpanNode</a></span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return the first immediate child that satisfies the given predicate, or None if none match.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span></pre></div></td><td class="code"><div><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">first_child</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SpanNode</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return the first immediate child that satisfies the given predicate, or None if none match."""</span>
    <span class="k">return</span> <span class="nb">next</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_filter_children</span><span class="p">(</span><span class="n">predicate</span><span class="p">),</span> <span class="kc">None</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.otel.SpanNode.any_child" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">any_child</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code><span class="nf">any_child</span><span class="p">(</span><span class="n">predicate</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Returns True if there is at least one child that satisfies the predicate.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span></pre></div></td><td class="code"><div><pre id="__code_11"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_11 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">any_child</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Returns True if there is at least one child that satisfies the predicate."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">first_child</span><span class="p">(</span><span class="n">predicate</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.otel.SpanNode.find_descendants" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">find_descendants</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code><span class="nf">find_descendants</span><span class="p">(</span>
    <span class="n">predicate</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span><span class="p">,</span>
    <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanNode" href="#pydantic_evals.otel.SpanNode">SpanNode</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return all descendant nodes that satisfy the given predicate in DFS order.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span></pre></div></td><td class="code"><div><pre id="__code_13"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_13 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">find_descendants</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Return all descendant nodes that satisfy the given predicate in DFS order."""</span>
    <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_filter_descendants</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.otel.SpanNode.first_descendant" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">first_descendant</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_14"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_14 > code"></button><code><span class="nf">first_descendant</span><span class="p">(</span>
    <span class="n">predicate</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span><span class="p">,</span>
    <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanNode" href="#pydantic_evals.otel.SpanNode">SpanNode</a></span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>DFS: Return the first descendant (in DFS order) that satisfies the given predicate, or <code>None</code> if none match.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span></pre></div></td><td class="code"><div><pre id="__code_15"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_15 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">first_descendant</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SpanNode</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""DFS: Return the first descendant (in DFS order) that satisfies the given predicate, or `None` if none match."""</span>
    <span class="k">return</span> <span class="nb">next</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_filter_descendants</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">),</span> <span class="kc">None</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.otel.SpanNode.any_descendant" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">any_descendant</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_16"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_16 > code"></button><code><span class="nf">any_descendant</span><span class="p">(</span>
    <span class="n">predicate</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span><span class="p">,</span>
    <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Returns <code>True</code> if there is at least one descendant that satisfies the predicate.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span></pre></div></td><td class="code"><div><pre id="__code_17"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_17 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">any_descendant</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Returns `True` if there is at least one descendant that satisfies the predicate."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">first_descendant</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.otel.SpanNode.find_ancestors" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">find_ancestors</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_18"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_18 > code"></button><code><span class="nf">find_ancestors</span><span class="p">(</span>
    <span class="n">predicate</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span><span class="p">,</span>
    <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanNode" href="#pydantic_evals.otel.SpanNode">SpanNode</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return all ancestors that satisfy the given predicate.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span></pre></div></td><td class="code"><div><pre id="__code_19"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_19 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">find_ancestors</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Return all ancestors that satisfy the given predicate."""</span>
    <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_filter_ancestors</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.otel.SpanNode.first_ancestor" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">first_ancestor</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_20"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_20 > code"></button><code><span class="nf">first_ancestor</span><span class="p">(</span>
    <span class="n">predicate</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span><span class="p">,</span>
    <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanNode" href="#pydantic_evals.otel.SpanNode">SpanNode</a></span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return the closest ancestor that satisfies the given predicate, or <code>None</code> if none match.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span></pre></div></td><td class="code"><div><pre id="__code_21"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_21 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">first_ancestor</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SpanNode</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return the closest ancestor that satisfies the given predicate, or `None` if none match."""</span>
    <span class="k">return</span> <span class="nb">next</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_filter_ancestors</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">),</span> <span class="kc">None</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.otel.SpanNode.any_ancestor" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">any_ancestor</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_22"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_22 > code"></button><code><span class="nf">any_ancestor</span><span class="p">(</span>
    <span class="n">predicate</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span><span class="p">,</span>
    <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Returns True if any ancestor satisfies the predicate.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span></pre></div></td><td class="code"><div><pre id="__code_23"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_23 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">any_ancestor</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Returns True if any ancestor satisfies the predicate."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">first_ancestor</span><span class="p">(</span><span class="n">predicate</span><span class="p">,</span> <span class="n">stop_recursing_when</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.otel.SpanNode.matches" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">matches</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_24"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_24 > code"></button><code><span class="nf">matches</span><span class="p">(</span><span class="n">query</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Check if the span node matches the query conditions or predicate.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span></pre></div></td><td class="code"><div><pre id="__code_25"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_25 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">matches</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Check if the span node matches the query conditions or predicate."""</span>
    <span class="k">if</span> <span class="nb">callable</span><span class="p">(</span><span class="n">query</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">query</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_matches_query</span><span class="p">(</span><span class="n">query</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>










<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.otel.SpanNode.repr_xml" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">repr_xml</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_26"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_26 > code"></button><code><span class="nf">repr_xml</span><span class="p">(</span>
    <span class="n">include_children</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">include_trace_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_span_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_start_timestamp</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_duration</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return an XML-like string representation of the node.</p>
<p>Optionally includes children, trace_id, span_id, start_timestamp, and duration.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">380</span>
<span class="normal">381</span>
<span class="normal">382</span>
<span class="normal">383</span>
<span class="normal">384</span>
<span class="normal">385</span>
<span class="normal">386</span>
<span class="normal">387</span>
<span class="normal">388</span>
<span class="normal">389</span>
<span class="normal">390</span>
<span class="normal">391</span>
<span class="normal">392</span>
<span class="normal">393</span>
<span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span>
<span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span>
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span>
<span class="normal">417</span>
<span class="normal">418</span>
<span class="normal">419</span>
<span class="normal">420</span>
<span class="normal">421</span>
<span class="normal">422</span>
<span class="normal">423</span></pre></div></td><td class="code"><div><pre id="__code_27"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_27 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">repr_xml</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">include_children</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">include_trace_id</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_span_id</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_start_timestamp</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_duration</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return an XML-like string representation of the node.</span>

<span class="sd">    Optionally includes children, trace_id, span_id, start_timestamp, and duration.</span>
<span class="sd">    """</span>
    <span class="n">first_line_parts</span> <span class="o">=</span> <span class="p">[</span><span class="sa">f</span><span class="s1">'&lt;SpanNode name=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">!r}</span><span class="s1">'</span><span class="p">]</span>
    <span class="k">if</span> <span class="n">include_trace_id</span><span class="p">:</span>
        <span class="n">first_line_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"trace_id='</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">trace_id</span><span class="si">:</span><span class="s2">032x</span><span class="si">}</span><span class="s2">'"</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">include_span_id</span><span class="p">:</span>
        <span class="n">first_line_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"span_id='</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">span_id</span><span class="si">:</span><span class="s2">016x</span><span class="si">}</span><span class="s2">'"</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">include_start_timestamp</span><span class="p">:</span>
        <span class="n">first_line_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">'start_timestamp=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">start_timestamp</span><span class="o">.</span><span class="n">isoformat</span><span class="p">()</span><span class="si">!r}</span><span class="s1">'</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">include_duration</span><span class="p">:</span>
        <span class="n">first_line_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"duration='</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">duration</span><span class="si">}</span><span class="s2">'"</span><span class="p">)</span>

    <span class="n">extra_lines</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">if</span> <span class="n">include_children</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">:</span>
        <span class="n">first_line_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">'&gt;'</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">child</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">:</span>
            <span class="n">extra_lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">indent</span><span class="p">(</span>
                    <span class="n">child</span><span class="o">.</span><span class="n">repr_xml</span><span class="p">(</span>
                        <span class="n">include_children</span><span class="o">=</span><span class="n">include_children</span><span class="p">,</span>
                        <span class="n">include_trace_id</span><span class="o">=</span><span class="n">include_trace_id</span><span class="p">,</span>
                        <span class="n">include_span_id</span><span class="o">=</span><span class="n">include_span_id</span><span class="p">,</span>
                        <span class="n">include_start_timestamp</span><span class="o">=</span><span class="n">include_start_timestamp</span><span class="p">,</span>
                        <span class="n">include_duration</span><span class="o">=</span><span class="n">include_duration</span><span class="p">,</span>
                    <span class="p">),</span>
                    <span class="s1">'  '</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>
        <span class="n">extra_lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">'&lt;/SpanNode&gt;'</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">children</span><span class="p">:</span>
            <span class="n">first_line_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">'children=...'</span><span class="p">)</span>
        <span class="n">first_line_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">'/&gt;'</span><span class="p">)</span>
    <span class="k">return</span> <span class="s1">'</span><span class="se">\n</span><span class="s1">'</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="s1">' '</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">first_line_parts</span><span class="p">),</span> <span class="o">*</span><span class="n">extra_lines</span><span class="p">])</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.otel.SpanQuery" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">SpanQuery</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing_extensions.TypedDict" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict">TypedDict</a></code></p>


        <p>A serializable query for filtering SpanNodes based on various conditions.</p>
<p>All fields are optional and combined with AND logic by default.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span></pre></div></td><td class="code"><div><pre id="__code_28"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_28 > code"></button><code><span class="k">class</span><span class="w"> </span><span class="nc">SpanQuery</span><span class="p">(</span><span class="n">TypedDict</span><span class="p">,</span> <span class="n">total</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""A serializable query for filtering SpanNodes based on various conditions.</span>

<span class="sd">    All fields are optional and combined with AND logic by default.</span>
<span class="sd">    """</span>

    <span class="c1"># These fields are ordered to match the implementation of SpanNode.matches_query for easy review.</span>
    <span class="c1"># * Individual span conditions come first because these are generally the cheapest to evaluate</span>
    <span class="c1"># * Logical combinations come next because they may just be combinations of individual span conditions</span>
    <span class="c1"># * Related-span conditions come last because they may require the most work to evaluate</span>

    <span class="c1"># Individual span conditions</span>
    <span class="c1">## Name conditions</span>
    <span class="n">name_equals</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">name_contains</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">name_matches_regex</span><span class="p">:</span> <span class="nb">str</span>  <span class="c1"># regex pattern</span>

    <span class="c1">## Attribute conditions</span>
    <span class="n">has_attributes</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>
    <span class="n">has_attribute_keys</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>

    <span class="c1">## Timing conditions</span>
    <span class="n">min_duration</span><span class="p">:</span> <span class="n">timedelta</span> <span class="o">|</span> <span class="nb">float</span>
    <span class="n">max_duration</span><span class="p">:</span> <span class="n">timedelta</span> <span class="o">|</span> <span class="nb">float</span>

    <span class="c1"># Logical combinations of conditions</span>
    <span class="n">not_</span><span class="p">:</span> <span class="n">SpanQuery</span>
    <span class="n">and_</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">SpanQuery</span><span class="p">]</span>
    <span class="n">or_</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">SpanQuery</span><span class="p">]</span>

    <span class="c1"># Child conditions</span>
    <span class="n">min_child_count</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">max_child_count</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">some_child_has</span><span class="p">:</span> <span class="n">SpanQuery</span>
    <span class="n">all_children_have</span><span class="p">:</span> <span class="n">SpanQuery</span>
    <span class="n">no_child_has</span><span class="p">:</span> <span class="n">SpanQuery</span>

    <span class="c1"># Recursive conditions</span>
    <span class="n">stop_recursing_when</span><span class="p">:</span> <span class="n">SpanQuery</span>
<span class="w">    </span><span class="sd">"""If present, stop recursing through ancestors or descendants at nodes that match this condition."""</span>

    <span class="c1">## Descendant conditions</span>
    <span class="n">min_descendant_count</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">max_descendant_count</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">some_descendant_has</span><span class="p">:</span> <span class="n">SpanQuery</span>
    <span class="n">all_descendants_have</span><span class="p">:</span> <span class="n">SpanQuery</span>
    <span class="n">no_descendant_has</span><span class="p">:</span> <span class="n">SpanQuery</span>

    <span class="c1">## Ancestor conditions</span>
    <span class="n">min_depth</span><span class="p">:</span> <span class="nb">int</span>  <span class="c1"># depth is equivalent to ancestor count; roots have depth 0</span>
    <span class="n">max_depth</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">some_ancestor_has</span><span class="p">:</span> <span class="n">SpanQuery</span>
    <span class="n">all_ancestors_have</span><span class="p">:</span> <span class="n">SpanQuery</span>
    <span class="n">no_ancestor_has</span><span class="p">:</span> <span class="n">SpanQuery</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.otel.SpanQuery.stop_recursing_when" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">stop_recursing_when</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_29"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_29 > code"></button><code><span class="n">stop_recursing_when</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>If present, stop recursing through ancestors or descendants at nodes that match this condition.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.otel.SpanTree" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">SpanTree</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>A container that builds a hierarchy of SpanNode objects from a list of finished spans.</p>
<p>You can then search or iterate the tree to make your assertions (using DFS for traversal).</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">438</span>
<span class="normal">439</span>
<span class="normal">440</span>
<span class="normal">441</span>
<span class="normal">442</span>
<span class="normal">443</span>
<span class="normal">444</span>
<span class="normal">445</span>
<span class="normal">446</span>
<span class="normal">447</span>
<span class="normal">448</span>
<span class="normal">449</span>
<span class="normal">450</span>
<span class="normal">451</span>
<span class="normal">452</span>
<span class="normal">453</span>
<span class="normal">454</span>
<span class="normal">455</span>
<span class="normal">456</span>
<span class="normal">457</span>
<span class="normal">458</span>
<span class="normal">459</span>
<span class="normal">460</span>
<span class="normal">461</span>
<span class="normal">462</span>
<span class="normal">463</span>
<span class="normal">464</span>
<span class="normal">465</span>
<span class="normal">466</span>
<span class="normal">467</span>
<span class="normal">468</span>
<span class="normal">469</span>
<span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span>
<span class="normal">473</span>
<span class="normal">474</span>
<span class="normal">475</span>
<span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span>
<span class="normal">495</span>
<span class="normal">496</span>
<span class="normal">497</span>
<span class="normal">498</span>
<span class="normal">499</span>
<span class="normal">500</span>
<span class="normal">501</span>
<span class="normal">502</span>
<span class="normal">503</span>
<span class="normal">504</span>
<span class="normal">505</span>
<span class="normal">506</span>
<span class="normal">507</span>
<span class="normal">508</span>
<span class="normal">509</span>
<span class="normal">510</span>
<span class="normal">511</span>
<span class="normal">512</span>
<span class="normal">513</span>
<span class="normal">514</span>
<span class="normal">515</span>
<span class="normal">516</span>
<span class="normal">517</span>
<span class="normal">518</span>
<span class="normal">519</span>
<span class="normal">520</span>
<span class="normal">521</span>
<span class="normal">522</span>
<span class="normal">523</span>
<span class="normal">524</span>
<span class="normal">525</span>
<span class="normal">526</span>
<span class="normal">527</span>
<span class="normal">528</span>
<span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span>
<span class="normal">541</span>
<span class="normal">542</span>
<span class="normal">543</span>
<span class="normal">544</span>
<span class="normal">545</span>
<span class="normal">546</span></pre></div></td><td class="code"><div><pre id="__code_30"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_30 > code"></button><code tabindex="0"><span class="nd">@dataclass</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="k">class</span><span class="w"> </span><span class="nc">SpanTree</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""A container that builds a hierarchy of SpanNode objects from a list of finished spans.</span>

<span class="sd">    You can then search or iterate the tree to make your assertions (using DFS for traversal).</span>
<span class="sd">    """</span>

    <span class="n">roots</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">]</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">)</span>
    <span class="n">nodes_by_id</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">SpanNode</span><span class="p">]</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">)</span>

    <span class="c1"># -------------------------------------------------------------------------</span>
    <span class="c1"># Construction</span>
    <span class="c1"># -------------------------------------------------------------------------</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">__post_init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_rebuild_tree</span><span class="p">()</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">add_spans</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">spans</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Add a list of spans to the tree, rebuilding the tree structure."""</span>
        <span class="k">for</span> <span class="n">span</span> <span class="ow">in</span> <span class="n">spans</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">nodes_by_id</span><span class="p">[</span><span class="n">span</span><span class="o">.</span><span class="n">node_key</span><span class="p">]</span> <span class="o">=</span> <span class="n">span</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_rebuild_tree</span><span class="p">()</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">add_readable_spans</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">readable_spans</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ReadableSpan</span><span class="p">]):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">add_spans</span><span class="p">([</span><span class="n">SpanNode</span><span class="o">.</span><span class="n">from_readable_span</span><span class="p">(</span><span class="n">span</span><span class="p">)</span> <span class="k">for</span> <span class="n">span</span> <span class="ow">in</span> <span class="n">readable_spans</span><span class="p">])</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_rebuild_tree</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="c1"># Ensure spans are ordered by start_timestamp so that roots and children end up in the right order</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">nodes_by_id</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>
        <span class="n">nodes</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">node</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">start_timestamp</span> <span class="ow">or</span> <span class="n">datetime</span><span class="o">.</span><span class="n">min</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">nodes_by_id</span> <span class="o">=</span> <span class="p">{</span><span class="n">node</span><span class="o">.</span><span class="n">node_key</span><span class="p">:</span> <span class="n">node</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">}</span>

        <span class="c1"># Build the parent/child relationships</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">nodes_by_id</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
            <span class="n">parent_node_key</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">parent_node_key</span>
            <span class="k">if</span> <span class="n">parent_node_key</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">parent_node</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">nodes_by_id</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">parent_node_key</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">parent_node</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="n">parent_node</span><span class="o">.</span><span class="n">add_child</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

        <span class="c1"># Determine the roots</span>
        <span class="c1"># A node is a "root" if its parent is None or if its parent's span_id is not in the current set of spans.</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">roots</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">nodes_by_id</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
            <span class="n">parent_node_key</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">parent_node_key</span>
            <span class="k">if</span> <span class="n">parent_node_key</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">parent_node_key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">nodes_by_id</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">roots</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

    <span class="c1"># -------------------------------------------------------------------------</span>
    <span class="c1"># Node filtering and iteration</span>
    <span class="c1"># -------------------------------------------------------------------------</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">find</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Find all nodes in the entire tree that match the predicate, scanning from each root in DFS order."""</span>
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_filter</span><span class="p">(</span><span class="n">predicate</span><span class="p">))</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">first</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SpanNode</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Find the first node that matches a predicate, scanning from each root in DFS order. Returns `None` if not found."""</span>
        <span class="k">return</span> <span class="nb">next</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_filter</span><span class="p">(</span><span class="n">predicate</span><span class="p">),</span> <span class="kc">None</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">any</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Returns True if any node in the tree matches the predicate."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">first</span><span class="p">(</span><span class="n">predicate</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_filter</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterator</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">]:</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="bp">self</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">matches</span><span class="p">(</span><span class="n">predicate</span><span class="p">):</span>
                <span class="k">yield</span> <span class="n">node</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__iter__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterator</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Return an iterator over all nodes in the tree."""</span>
        <span class="k">return</span> <span class="nb">iter</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">nodes_by_id</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>

    <span class="c1"># -------------------------------------------------------------------------</span>
    <span class="c1"># String representation</span>
    <span class="c1"># -------------------------------------------------------------------------</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">repr_xml</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">include_children</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">include_trace_id</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">include_span_id</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">include_start_timestamp</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">include_duration</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return an XML-like string representation of the tree, optionally including children, trace_id, span_id, duration, and timestamps."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">roots</span><span class="p">:</span>
            <span class="k">return</span> <span class="s1">'&lt;SpanTree /&gt;'</span>
        <span class="n">repr_parts</span> <span class="o">=</span> <span class="p">[</span>
            <span class="s1">'&lt;SpanTree&gt;'</span><span class="p">,</span>
            <span class="o">*</span><span class="p">[</span>
                <span class="n">indent</span><span class="p">(</span>
                    <span class="n">root</span><span class="o">.</span><span class="n">repr_xml</span><span class="p">(</span>
                        <span class="n">include_children</span><span class="o">=</span><span class="n">include_children</span><span class="p">,</span>
                        <span class="n">include_trace_id</span><span class="o">=</span><span class="n">include_trace_id</span><span class="p">,</span>
                        <span class="n">include_span_id</span><span class="o">=</span><span class="n">include_span_id</span><span class="p">,</span>
                        <span class="n">include_start_timestamp</span><span class="o">=</span><span class="n">include_start_timestamp</span><span class="p">,</span>
                        <span class="n">include_duration</span><span class="o">=</span><span class="n">include_duration</span><span class="p">,</span>
                    <span class="p">),</span>
                    <span class="s1">'  '</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="k">for</span> <span class="n">root</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">roots</span>
            <span class="p">],</span>
            <span class="s1">'&lt;/SpanTree&gt;'</span><span class="p">,</span>
        <span class="p">]</span>
        <span class="k">return</span> <span class="s1">'</span><span class="se">\n</span><span class="s1">'</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">repr_parts</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s1">'&lt;SpanTree num_roots=</span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">roots</span><span class="p">)</span><span class="si">}</span><span class="s1"> total_spans=</span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">nodes_by_id</span><span class="p">)</span><span class="si">}</span><span class="s1"> /&gt;'</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">repr_xml</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.otel.SpanTree.add_spans" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">add_spans</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_31"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_31 > code"></button><code><span class="nf">add_spans</span><span class="p">(</span><span class="n">spans</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanNode" href="#pydantic_evals.otel.SpanNode">SpanNode</a></span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Add a list of spans to the tree, rebuilding the tree structure.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">454</span>
<span class="normal">455</span>
<span class="normal">456</span>
<span class="normal">457</span>
<span class="normal">458</span></pre></div></td><td class="code"><div><pre id="__code_32"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_32 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">add_spans</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">spans</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Add a list of spans to the tree, rebuilding the tree structure."""</span>
    <span class="k">for</span> <span class="n">span</span> <span class="ow">in</span> <span class="n">spans</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">nodes_by_id</span><span class="p">[</span><span class="n">span</span><span class="o">.</span><span class="n">node_key</span><span class="p">]</span> <span class="o">=</span> <span class="n">span</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_rebuild_tree</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.otel.SpanTree.find" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">find</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_33"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_33 > code"></button><code><span class="nf">find</span><span class="p">(</span>
    <span class="n">predicate</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanNode" href="#pydantic_evals.otel.SpanNode">SpanNode</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Find all nodes in the entire tree that match the predicate, scanning from each root in DFS order.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span></pre></div></td><td class="code"><div><pre id="__code_34"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_34 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">find</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Find all nodes in the entire tree that match the predicate, scanning from each root in DFS order."""</span>
    <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_filter</span><span class="p">(</span><span class="n">predicate</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.otel.SpanTree.first" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">first</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_35"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_35 > code"></button><code><span class="nf">first</span><span class="p">(</span>
    <span class="n">predicate</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanNode" href="#pydantic_evals.otel.SpanNode">SpanNode</a></span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Find the first node that matches a predicate, scanning from each root in DFS order. Returns <code>None</code> if not found.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span></pre></div></td><td class="code"><div><pre id="__code_36"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_36 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">first</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SpanNode</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Find the first node that matches a predicate, scanning from each root in DFS order. Returns `None` if not found."""</span>
    <span class="k">return</span> <span class="nb">next</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_filter</span><span class="p">(</span><span class="n">predicate</span><span class="p">),</span> <span class="kc">None</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.otel.SpanTree.any" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">any</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_37"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_37 > code"></button><code><span class="nb">any</span><span class="p">(</span><span class="nf">predicate</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanQuery" href="#pydantic_evals.otel.SpanQuery">SpanQuery</a></span> <span class="o">|</span> <span class="n"><span title="pydantic_evals.otel.span_tree.SpanPredicate">SpanPredicate</span></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Returns True if any node in the tree matches the predicate.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">496</span>
<span class="normal">497</span>
<span class="normal">498</span></pre></div></td><td class="code"><div><pre id="__code_38"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_38 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">any</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">predicate</span><span class="p">:</span> <span class="n">SpanQuery</span> <span class="o">|</span> <span class="n">SpanPredicate</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Returns True if any node in the tree matches the predicate."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">first</span><span class="p">(</span><span class="n">predicate</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.otel.SpanTree.__iter__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__iter__</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_39"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_39 > code"></button><code><span class="fm">__iter__</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="nf"><a class="autorefs autorefs-external" title="collections.abc.Iterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator">Iterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanNode" href="#pydantic_evals.otel.SpanNode">SpanNode</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return an iterator over all nodes in the tree.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">505</span>
<span class="normal">506</span>
<span class="normal">507</span></pre></div></td><td class="code"><div><pre id="__code_40"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_40 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="fm">__iter__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterator</span><span class="p">[</span><span class="n">SpanNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Return an iterator over all nodes in the tree."""</span>
    <span class="k">return</span> <span class="nb">iter</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">nodes_by_id</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.otel.SpanTree.repr_xml" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">repr_xml</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_41"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_41 > code"></button><code><span class="nf">repr_xml</span><span class="p">(</span>
    <span class="n">include_children</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">include_trace_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_span_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_start_timestamp</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_duration</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return an XML-like string representation of the tree, optionally including children, trace_id, span_id, duration, and timestamps.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/otel/span_tree.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">512</span>
<span class="normal">513</span>
<span class="normal">514</span>
<span class="normal">515</span>
<span class="normal">516</span>
<span class="normal">517</span>
<span class="normal">518</span>
<span class="normal">519</span>
<span class="normal">520</span>
<span class="normal">521</span>
<span class="normal">522</span>
<span class="normal">523</span>
<span class="normal">524</span>
<span class="normal">525</span>
<span class="normal">526</span>
<span class="normal">527</span>
<span class="normal">528</span>
<span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span></pre></div></td><td class="code"><div><pre id="__code_42"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_42 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">repr_xml</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">include_children</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">include_trace_id</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_span_id</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_start_timestamp</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_duration</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return an XML-like string representation of the tree, optionally including children, trace_id, span_id, duration, and timestamps."""</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">roots</span><span class="p">:</span>
        <span class="k">return</span> <span class="s1">'&lt;SpanTree /&gt;'</span>
    <span class="n">repr_parts</span> <span class="o">=</span> <span class="p">[</span>
        <span class="s1">'&lt;SpanTree&gt;'</span><span class="p">,</span>
        <span class="o">*</span><span class="p">[</span>
            <span class="n">indent</span><span class="p">(</span>
                <span class="n">root</span><span class="o">.</span><span class="n">repr_xml</span><span class="p">(</span>
                    <span class="n">include_children</span><span class="o">=</span><span class="n">include_children</span><span class="p">,</span>
                    <span class="n">include_trace_id</span><span class="o">=</span><span class="n">include_trace_id</span><span class="p">,</span>
                    <span class="n">include_span_id</span><span class="o">=</span><span class="n">include_span_id</span><span class="p">,</span>
                    <span class="n">include_start_timestamp</span><span class="o">=</span><span class="n">include_start_timestamp</span><span class="p">,</span>
                    <span class="n">include_duration</span><span class="o">=</span><span class="n">include_duration</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="s1">'  '</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">root</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">roots</span>
        <span class="p">],</span>
        <span class="s1">'&lt;/SpanTree&gt;'</span><span class="p">,</span>
    <span class="p">]</span>
    <span class="k">return</span> <span class="s1">'</span><span class="se">\n</span><span class="s1">'</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">repr_parts</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>




  </div>

    </div>

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
    
    
    <script id="__config" type="application/json">{"base": "../../..", "features": ["search.suggest", "search.highlight", "content.tabs.link", "content.code.annotate", "content.code.copy", "content.code.select", "navigation.path", "navigation.indexes", "navigation.sections", "navigation.tracking", "toc.follow"], "search": "../../../assets/javascripts/workers/search.f8cc74c7.min.js", "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}}</script>
    
    
      <script src="../../../assets/javascripts/bundle.f1b6f286.min.js"></script>
      
        <script src="/flarelytics/client.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/algoliasearch@5.20.0/dist/lite/builds/browser.umd.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4.77.3/dist/instantsearch.production.min.js"></script>
      
        <script src="/javascripts/algolia-search.js"></script>
      
    
  <script id="init-glightbox">const lightbox = GLightbox({"touchNavigation": true, "loop": false, "zoomable": true, "draggable": true, "openEffect": "zoom", "closeEffect": "zoom", "slideEffect": "slide"});
document$.subscribe(() => { lightbox.reload() });
</script>
</body></html>