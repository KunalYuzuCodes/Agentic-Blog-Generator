<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/api/pydantic_evals/reporting/">
      
      
        <link rel="prev" href="../evaluators/">
      
      
        <link rel="next" href="../otel/">
      
      
      <link rel="icon" href="../../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>pydantic_evals.reporting - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="pydantic_evals.reporting - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/api/pydantic_evals/reporting.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/api/pydantic_evals/reporting/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="pydantic_evals.reporting - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/api/pydantic_evals/reporting.png">
      
    
    
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
      
        
        <a href="#pydantic_evalsreporting" class="md-skip">
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
            
              pydantic_evals.reporting
            
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
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.reporting" class="md-nav__link">
    <span class="md-ellipsis">
      reporting
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.ReportCase" class="md-nav__link">
    <span class="md-ellipsis">
      ReportCase
    </span>
  </a>
  
    <nav class="md-nav" aria-label="ReportCase">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.ReportCase.name" class="md-nav__link">
    <span class="md-ellipsis">
      name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.ReportCase.inputs" class="md-nav__link">
    <span class="md-ellipsis">
      inputs
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.ReportCase.metadata" class="md-nav__link">
    <span class="md-ellipsis">
      metadata
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.ReportCase.expected_output" class="md-nav__link">
    <span class="md-ellipsis">
      expected_output
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.ReportCase.output" class="md-nav__link">
    <span class="md-ellipsis">
      output
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.ReportCaseAggregate" class="md-nav__link">
    <span class="md-ellipsis">
      ReportCaseAggregate
    </span>
  </a>
  
    <nav class="md-nav" aria-label="ReportCaseAggregate">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.ReportCaseAggregate.average" class="md-nav__link">
    <span class="md-ellipsis">
      average
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.EvaluationReport" class="md-nav__link">
    <span class="md-ellipsis">
      EvaluationReport
    </span>
  </a>
  
    <nav class="md-nav" aria-label="EvaluationReport">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.EvaluationReport.name" class="md-nav__link">
    <span class="md-ellipsis">
      name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.EvaluationReport.cases" class="md-nav__link">
    <span class="md-ellipsis">
      cases
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.EvaluationReport.print" class="md-nav__link">
    <span class="md-ellipsis">
      print
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.EvaluationReport.console_table" class="md-nav__link">
    <span class="md-ellipsis">
      console_table
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.EvaluationReport.__str__" class="md-nav__link">
    <span class="md-ellipsis">
      __str__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.RenderValueConfig" class="md-nav__link">
    <span class="md-ellipsis">
      RenderValueConfig
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.RenderNumberConfig" class="md-nav__link">
    <span class="md-ellipsis">
      RenderNumberConfig
    </span>
  </a>
  
    <nav class="md-nav" aria-label="RenderNumberConfig">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.RenderNumberConfig.value_formatter" class="md-nav__link">
    <span class="md-ellipsis">
      value_formatter
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.RenderNumberConfig.diff_formatter" class="md-nav__link">
    <span class="md-ellipsis">
      diff_formatter
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.RenderNumberConfig.diff_atol" class="md-nav__link">
    <span class="md-ellipsis">
      diff_atol
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.RenderNumberConfig.diff_rtol" class="md-nav__link">
    <span class="md-ellipsis">
      diff_rtol
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.RenderNumberConfig.diff_increase_style" class="md-nav__link">
    <span class="md-ellipsis">
      diff_increase_style
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.RenderNumberConfig.diff_decrease_style" class="md-nav__link">
    <span class="md-ellipsis">
      diff_decrease_style
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.EvaluationRenderer" class="md-nav__link">
    <span class="md-ellipsis">
      EvaluationRenderer
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
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
  <a href="#pydantic_evals.reporting" class="md-nav__link">
    <span class="md-ellipsis">
      reporting
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.ReportCase" class="md-nav__link">
    <span class="md-ellipsis">
      ReportCase
    </span>
  </a>
  
    <nav class="md-nav" aria-label="ReportCase">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.ReportCase.name" class="md-nav__link">
    <span class="md-ellipsis">
      name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.ReportCase.inputs" class="md-nav__link">
    <span class="md-ellipsis">
      inputs
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.ReportCase.metadata" class="md-nav__link">
    <span class="md-ellipsis">
      metadata
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.ReportCase.expected_output" class="md-nav__link">
    <span class="md-ellipsis">
      expected_output
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.ReportCase.output" class="md-nav__link">
    <span class="md-ellipsis">
      output
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.ReportCaseAggregate" class="md-nav__link">
    <span class="md-ellipsis">
      ReportCaseAggregate
    </span>
  </a>
  
    <nav class="md-nav" aria-label="ReportCaseAggregate">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.ReportCaseAggregate.average" class="md-nav__link">
    <span class="md-ellipsis">
      average
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.EvaluationReport" class="md-nav__link">
    <span class="md-ellipsis">
      EvaluationReport
    </span>
  </a>
  
    <nav class="md-nav" aria-label="EvaluationReport">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.EvaluationReport.name" class="md-nav__link">
    <span class="md-ellipsis">
      name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.EvaluationReport.cases" class="md-nav__link">
    <span class="md-ellipsis">
      cases
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.EvaluationReport.print" class="md-nav__link">
    <span class="md-ellipsis">
      print
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.EvaluationReport.console_table" class="md-nav__link">
    <span class="md-ellipsis">
      console_table
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.EvaluationReport.__str__" class="md-nav__link">
    <span class="md-ellipsis">
      __str__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.RenderValueConfig" class="md-nav__link">
    <span class="md-ellipsis">
      RenderValueConfig
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.RenderNumberConfig" class="md-nav__link">
    <span class="md-ellipsis">
      RenderNumberConfig
    </span>
  </a>
  
    <nav class="md-nav" aria-label="RenderNumberConfig">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.RenderNumberConfig.value_formatter" class="md-nav__link">
    <span class="md-ellipsis">
      value_formatter
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.RenderNumberConfig.diff_formatter" class="md-nav__link">
    <span class="md-ellipsis">
      diff_formatter
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.RenderNumberConfig.diff_atol" class="md-nav__link">
    <span class="md-ellipsis">
      diff_atol
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.RenderNumberConfig.diff_rtol" class="md-nav__link">
    <span class="md-ellipsis">
      diff_rtol
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.RenderNumberConfig.diff_increase_style" class="md-nav__link">
    <span class="md-ellipsis">
      diff_increase_style
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.RenderNumberConfig.diff_decrease_style" class="md-nav__link">
    <span class="md-ellipsis">
      diff_decrease_style
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.reporting.EvaluationRenderer" class="md-nav__link">
    <span class="md-ellipsis">
      EvaluationRenderer
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
                
                  


  
  


<h1 id="pydantic_evalsreporting"><code>pydantic_evals.reporting</code></h1>


<div class="doc doc-object doc-module">



<a id="pydantic_evals.reporting"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">











































<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.reporting.ReportCase" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">ReportCase</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="pydantic.BaseModel" href="https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel">BaseModel</a></code></p>


        <p>A single case in an evaluation report.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/reporting/__init__.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">39</span>
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
<span class="normal">65</span></pre></div></td><td class="code"><div><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="k">class</span><span class="w"> </span><span class="nc">ReportCase</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""A single case in an evaluation report."""</span>

    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""The name of the [case][pydantic_evals.Case]."""</span>
    <span class="n">inputs</span><span class="p">:</span> <span class="n">Any</span>
<span class="w">    </span><span class="sd">"""The inputs to the task, from [`Case.inputs`][pydantic_evals.Case.inputs]."""</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n">Any</span>
<span class="w">    </span><span class="sd">"""Any metadata associated with the case, from [`Case.metadata`][pydantic_evals.Case.metadata]."""</span>
    <span class="n">expected_output</span><span class="p">:</span> <span class="n">Any</span>
<span class="w">    </span><span class="sd">"""The expected output of the task, from [`Case.expected_output`][pydantic_evals.Case.expected_output]."""</span>
    <span class="n">output</span><span class="p">:</span> <span class="n">Any</span>
<span class="w">    </span><span class="sd">"""The output of the task execution."""</span>

    <span class="n">metrics</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span> <span class="o">|</span> <span class="nb">int</span><span class="p">]</span>
    <span class="n">attributes</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>

    <span class="n">scores</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">EvaluationResult</span><span class="p">[</span><span class="nb">int</span> <span class="o">|</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">labels</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">EvaluationResult</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">assertions</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">EvaluationResult</span><span class="p">[</span><span class="nb">bool</span><span class="p">]]</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="n">task_duration</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">total_duration</span><span class="p">:</span> <span class="nb">float</span>  <span class="c1"># includes evaluator execution time</span>

    <span class="c1"># TODO(DavidM): Drop these once we can reference child spans in details panel:</span>
    <span class="n">trace_id</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">span_id</span><span class="p">:</span> <span class="nb">str</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.reporting.ReportCase.name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code><span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The name of the <a class="autorefs autorefs-internal" href="../dataset/#pydantic_evals.dataset.Case">case</a>.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.reporting.ReportCase.inputs" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">inputs</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="n">inputs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The inputs to the task, from <a class="autorefs autorefs-internal" href="../dataset/#pydantic_evals.dataset.Case.inputs"><code>Case.inputs</code></a>.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.reporting.ReportCase.metadata" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">metadata</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code><span class="n">metadata</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Any metadata associated with the case, from <a class="autorefs autorefs-internal" href="../dataset/#pydantic_evals.dataset.Case.metadata"><code>Case.metadata</code></a>.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.reporting.ReportCase.expected_output" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">expected_output</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code><span class="n">expected_output</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The expected output of the task, from <a class="autorefs autorefs-internal" href="../dataset/#pydantic_evals.dataset.Case.expected_output"><code>Case.expected_output</code></a>.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.reporting.ReportCase.output" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">output</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="n">output</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The output of the task execution.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.reporting.ReportCaseAggregate" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">ReportCaseAggregate</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="pydantic.BaseModel" href="https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel">BaseModel</a></code></p>


        <p>A synthetic case that summarizes a set of cases.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/reporting/__init__.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 68</span>
<span class="normal"> 69</span>
<span class="normal"> 70</span>
<span class="normal"> 71</span>
<span class="normal"> 72</span>
<span class="normal"> 73</span>
<span class="normal"> 74</span>
<span class="normal"> 75</span>
<span class="normal"> 76</span>
<span class="normal"> 77</span>
<span class="normal"> 78</span>
<span class="normal"> 79</span>
<span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
<span class="normal"> 83</span>
<span class="normal"> 84</span>
<span class="normal"> 85</span>
<span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
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
<span class="normal">142</span></pre></div></td><td class="code"><div><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code tabindex="0"><span class="k">class</span><span class="w"> </span><span class="nc">ReportCaseAggregate</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""A synthetic case that summarizes a set of cases."""</span>

    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>

    <span class="n">scores</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span> <span class="o">|</span> <span class="nb">int</span><span class="p">]</span>
    <span class="n">labels</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span>
    <span class="n">metrics</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span> <span class="o">|</span> <span class="nb">int</span><span class="p">]</span>
    <span class="n">assertions</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="n">task_duration</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">total_duration</span><span class="p">:</span> <span class="nb">float</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">average</span><span class="p">(</span><span class="n">cases</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ReportCase</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ReportCaseAggregate</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Produce a synthetic "summary" case by averaging quantitative attributes."""</span>
        <span class="n">num_cases</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">cases</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">num_cases</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">ReportCaseAggregate</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="s1">'Averages'</span><span class="p">,</span>
                <span class="n">scores</span><span class="o">=</span><span class="p">{},</span>
                <span class="n">labels</span><span class="o">=</span><span class="p">{},</span>
                <span class="n">metrics</span><span class="o">=</span><span class="p">{},</span>
                <span class="n">assertions</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
                <span class="n">task_duration</span><span class="o">=</span><span class="mf">0.0</span><span class="p">,</span>
                <span class="n">total_duration</span><span class="o">=</span><span class="mf">0.0</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="k">def</span><span class="w"> </span><span class="nf">_scores_averages</span><span class="p">(</span><span class="n">scores_by_name</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span> <span class="o">|</span> <span class="nb">float</span> <span class="o">|</span> <span class="nb">bool</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]:</span>
            <span class="n">counts_by_name</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>
            <span class="n">sums_by_name</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">float</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">sbn</span> <span class="ow">in</span> <span class="n">scores_by_name</span><span class="p">:</span>
                <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">score</span> <span class="ow">in</span> <span class="n">sbn</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                    <span class="n">counts_by_name</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
                    <span class="n">sums_by_name</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">+=</span> <span class="n">score</span>
            <span class="k">return</span> <span class="p">{</span><span class="n">name</span><span class="p">:</span> <span class="n">sums_by_name</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">/</span> <span class="n">counts_by_name</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">sums_by_name</span><span class="p">}</span>

        <span class="k">def</span><span class="w"> </span><span class="nf">_labels_averages</span><span class="p">(</span><span class="n">labels_by_name</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]:</span>
            <span class="n">counts_by_name</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>
            <span class="n">sums_by_name</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="k">lambda</span><span class="p">:</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">float</span><span class="p">))</span>
            <span class="k">for</span> <span class="n">lbn</span> <span class="ow">in</span> <span class="n">labels_by_name</span><span class="p">:</span>
                <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">label</span> <span class="ow">in</span> <span class="n">lbn</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                    <span class="n">counts_by_name</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
                    <span class="n">sums_by_name</span><span class="p">[</span><span class="n">name</span><span class="p">][</span><span class="n">label</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="k">return</span> <span class="p">{</span>
                <span class="n">name</span><span class="p">:</span> <span class="p">{</span><span class="n">value</span><span class="p">:</span> <span class="n">count</span> <span class="o">/</span> <span class="n">counts_by_name</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="k">for</span> <span class="n">value</span><span class="p">,</span> <span class="n">count</span> <span class="ow">in</span> <span class="n">sums_by_name</span><span class="p">[</span><span class="n">name</span><span class="p">]</span><span class="o">.</span><span class="n">items</span><span class="p">()}</span>
                <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">sums_by_name</span>
            <span class="p">}</span>

        <span class="n">average_task_duration</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">case</span><span class="o">.</span><span class="n">task_duration</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">cases</span><span class="p">)</span> <span class="o">/</span> <span class="n">num_cases</span>
        <span class="n">average_total_duration</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">case</span><span class="o">.</span><span class="n">total_duration</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">cases</span><span class="p">)</span> <span class="o">/</span> <span class="n">num_cases</span>

        <span class="c1"># average_assertions: dict[str, float] = _scores_averages([{k: v.value for k, v in case.scores.items()} for case in cases])</span>
        <span class="n">average_scores</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="n">_scores_averages</span><span class="p">(</span>
            <span class="p">[{</span><span class="n">k</span><span class="p">:</span> <span class="n">v</span><span class="o">.</span><span class="n">value</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">case</span><span class="o">.</span><span class="n">scores</span><span class="o">.</span><span class="n">items</span><span class="p">()}</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">cases</span><span class="p">]</span>
        <span class="p">)</span>
        <span class="n">average_labels</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="n">_labels_averages</span><span class="p">(</span>
            <span class="p">[{</span><span class="n">k</span><span class="p">:</span> <span class="n">v</span><span class="o">.</span><span class="n">value</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">case</span><span class="o">.</span><span class="n">labels</span><span class="o">.</span><span class="n">items</span><span class="p">()}</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">cases</span><span class="p">]</span>
        <span class="p">)</span>
        <span class="n">average_metrics</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="n">_scores_averages</span><span class="p">([</span><span class="n">case</span><span class="o">.</span><span class="n">metrics</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">cases</span><span class="p">])</span>

        <span class="n">average_assertions</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">n_assertions</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">case</span><span class="o">.</span><span class="n">assertions</span><span class="p">)</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">cases</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">n_assertions</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">n_passing</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="mi">1</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">cases</span> <span class="k">for</span> <span class="n">assertion</span> <span class="ow">in</span> <span class="n">case</span><span class="o">.</span><span class="n">assertions</span><span class="o">.</span><span class="n">values</span><span class="p">()</span> <span class="k">if</span> <span class="n">assertion</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
            <span class="n">average_assertions</span> <span class="o">=</span> <span class="n">n_passing</span> <span class="o">/</span> <span class="n">n_assertions</span>

        <span class="k">return</span> <span class="n">ReportCaseAggregate</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="s1">'Averages'</span><span class="p">,</span>
            <span class="n">scores</span><span class="o">=</span><span class="n">average_scores</span><span class="p">,</span>
            <span class="n">labels</span><span class="o">=</span><span class="n">average_labels</span><span class="p">,</span>
            <span class="n">metrics</span><span class="o">=</span><span class="n">average_metrics</span><span class="p">,</span>
            <span class="n">assertions</span><span class="o">=</span><span class="n">average_assertions</span><span class="p">,</span>
            <span class="n">task_duration</span><span class="o">=</span><span class="n">average_task_duration</span><span class="p">,</span>
            <span class="n">total_duration</span><span class="o">=</span><span class="n">average_total_duration</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.reporting.ReportCaseAggregate.average" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">average</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-staticmethod"><code>staticmethod</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code><span class="nf">average</span><span class="p">(</span><span class="n">cases</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.ReportCase" href="#pydantic_evals.reporting.ReportCase">ReportCase</a></span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.ReportCaseAggregate" href="#pydantic_evals.reporting.ReportCaseAggregate">ReportCaseAggregate</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Produce a synthetic "summary" case by averaging quantitative attributes.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/reporting/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
<span class="normal"> 83</span>
<span class="normal"> 84</span>
<span class="normal"> 85</span>
<span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
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
<span class="normal">142</span></pre></div></td><td class="code"><div><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code tabindex="0"><span class="nd">@staticmethod</span>
<span class="k">def</span><span class="w"> </span><span class="nf">average</span><span class="p">(</span><span class="n">cases</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ReportCase</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ReportCaseAggregate</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Produce a synthetic "summary" case by averaging quantitative attributes."""</span>
    <span class="n">num_cases</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">cases</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">num_cases</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">ReportCaseAggregate</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="s1">'Averages'</span><span class="p">,</span>
            <span class="n">scores</span><span class="o">=</span><span class="p">{},</span>
            <span class="n">labels</span><span class="o">=</span><span class="p">{},</span>
            <span class="n">metrics</span><span class="o">=</span><span class="p">{},</span>
            <span class="n">assertions</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
            <span class="n">task_duration</span><span class="o">=</span><span class="mf">0.0</span><span class="p">,</span>
            <span class="n">total_duration</span><span class="o">=</span><span class="mf">0.0</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_scores_averages</span><span class="p">(</span><span class="n">scores_by_name</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span> <span class="o">|</span> <span class="nb">float</span> <span class="o">|</span> <span class="nb">bool</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]:</span>
        <span class="n">counts_by_name</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>
        <span class="n">sums_by_name</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">float</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">sbn</span> <span class="ow">in</span> <span class="n">scores_by_name</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">score</span> <span class="ow">in</span> <span class="n">sbn</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="n">counts_by_name</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
                <span class="n">sums_by_name</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">+=</span> <span class="n">score</span>
        <span class="k">return</span> <span class="p">{</span><span class="n">name</span><span class="p">:</span> <span class="n">sums_by_name</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">/</span> <span class="n">counts_by_name</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">sums_by_name</span><span class="p">}</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_labels_averages</span><span class="p">(</span><span class="n">labels_by_name</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]:</span>
        <span class="n">counts_by_name</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>
        <span class="n">sums_by_name</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="k">lambda</span><span class="p">:</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">float</span><span class="p">))</span>
        <span class="k">for</span> <span class="n">lbn</span> <span class="ow">in</span> <span class="n">labels_by_name</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">label</span> <span class="ow">in</span> <span class="n">lbn</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="n">counts_by_name</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
                <span class="n">sums_by_name</span><span class="p">[</span><span class="n">name</span><span class="p">][</span><span class="n">label</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="n">name</span><span class="p">:</span> <span class="p">{</span><span class="n">value</span><span class="p">:</span> <span class="n">count</span> <span class="o">/</span> <span class="n">counts_by_name</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="k">for</span> <span class="n">value</span><span class="p">,</span> <span class="n">count</span> <span class="ow">in</span> <span class="n">sums_by_name</span><span class="p">[</span><span class="n">name</span><span class="p">]</span><span class="o">.</span><span class="n">items</span><span class="p">()}</span>
            <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">sums_by_name</span>
        <span class="p">}</span>

    <span class="n">average_task_duration</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">case</span><span class="o">.</span><span class="n">task_duration</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">cases</span><span class="p">)</span> <span class="o">/</span> <span class="n">num_cases</span>
    <span class="n">average_total_duration</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">case</span><span class="o">.</span><span class="n">total_duration</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">cases</span><span class="p">)</span> <span class="o">/</span> <span class="n">num_cases</span>

    <span class="c1"># average_assertions: dict[str, float] = _scores_averages([{k: v.value for k, v in case.scores.items()} for case in cases])</span>
    <span class="n">average_scores</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="n">_scores_averages</span><span class="p">(</span>
        <span class="p">[{</span><span class="n">k</span><span class="p">:</span> <span class="n">v</span><span class="o">.</span><span class="n">value</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">case</span><span class="o">.</span><span class="n">scores</span><span class="o">.</span><span class="n">items</span><span class="p">()}</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">cases</span><span class="p">]</span>
    <span class="p">)</span>
    <span class="n">average_labels</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="n">_labels_averages</span><span class="p">(</span>
        <span class="p">[{</span><span class="n">k</span><span class="p">:</span> <span class="n">v</span><span class="o">.</span><span class="n">value</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">case</span><span class="o">.</span><span class="n">labels</span><span class="o">.</span><span class="n">items</span><span class="p">()}</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">cases</span><span class="p">]</span>
    <span class="p">)</span>
    <span class="n">average_metrics</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="n">_scores_averages</span><span class="p">([</span><span class="n">case</span><span class="o">.</span><span class="n">metrics</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">cases</span><span class="p">])</span>

    <span class="n">average_assertions</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">n_assertions</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">case</span><span class="o">.</span><span class="n">assertions</span><span class="p">)</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">cases</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">n_assertions</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">n_passing</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="mi">1</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">cases</span> <span class="k">for</span> <span class="n">assertion</span> <span class="ow">in</span> <span class="n">case</span><span class="o">.</span><span class="n">assertions</span><span class="o">.</span><span class="n">values</span><span class="p">()</span> <span class="k">if</span> <span class="n">assertion</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
        <span class="n">average_assertions</span> <span class="o">=</span> <span class="n">n_passing</span> <span class="o">/</span> <span class="n">n_assertions</span>

    <span class="k">return</span> <span class="n">ReportCaseAggregate</span><span class="p">(</span>
        <span class="n">name</span><span class="o">=</span><span class="s1">'Averages'</span><span class="p">,</span>
        <span class="n">scores</span><span class="o">=</span><span class="n">average_scores</span><span class="p">,</span>
        <span class="n">labels</span><span class="o">=</span><span class="n">average_labels</span><span class="p">,</span>
        <span class="n">metrics</span><span class="o">=</span><span class="n">average_metrics</span><span class="p">,</span>
        <span class="n">assertions</span><span class="o">=</span><span class="n">average_assertions</span><span class="p">,</span>
        <span class="n">task_duration</span><span class="o">=</span><span class="n">average_task_duration</span><span class="p">,</span>
        <span class="n">total_duration</span><span class="o">=</span><span class="n">average_total_duration</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.reporting.EvaluationReport" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">EvaluationReport</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="pydantic.BaseModel" href="https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel">BaseModel</a></code></p>


        <p>A report of the results of evaluating a model on a set of cases.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/reporting/__init__.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">145</span>
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
<span class="normal">250</span></pre></div></td><td class="code"><div><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code tabindex="0"><span class="k">class</span><span class="w"> </span><span class="nc">EvaluationReport</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""A report of the results of evaluating a model on a set of cases."""</span>

    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""The name of the report."""</span>
    <span class="n">cases</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ReportCase</span><span class="p">]</span>
<span class="w">    </span><span class="sd">"""The cases in the report."""</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">averages</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ReportCaseAggregate</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">ReportCaseAggregate</span><span class="o">.</span><span class="n">average</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">cases</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">print</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">width</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">baseline</span><span class="p">:</span> <span class="n">EvaluationReport</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">include_input</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">include_expected_output</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">include_output</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">include_durations</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">include_total_duration</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">include_removed_cases</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">include_averages</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">input_config</span><span class="p">:</span> <span class="n">RenderValueConfig</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">metadata_config</span><span class="p">:</span> <span class="n">RenderValueConfig</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">output_config</span><span class="p">:</span> <span class="n">RenderValueConfig</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">score_configs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RenderNumberConfig</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">label_configs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RenderValueConfig</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">metric_configs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RenderNumberConfig</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">duration_config</span><span class="p">:</span> <span class="n">RenderNumberConfig</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>  <span class="c1"># pragma: no cover</span>
<span class="w">        </span><span class="sd">"""Print this report to the console, optionally comparing it to a baseline report.</span>

<span class="sd">        If you want more control over the output, use `console_table` instead and pass it to `rich.Console.print`.</span>
<span class="sd">        """</span>
        <span class="n">table</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">console_table</span><span class="p">(</span>
            <span class="n">baseline</span><span class="o">=</span><span class="n">baseline</span><span class="p">,</span>
            <span class="n">include_input</span><span class="o">=</span><span class="n">include_input</span><span class="p">,</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
            <span class="n">include_expected_output</span><span class="o">=</span><span class="n">include_expected_output</span><span class="p">,</span>
            <span class="n">include_output</span><span class="o">=</span><span class="n">include_output</span><span class="p">,</span>
            <span class="n">include_durations</span><span class="o">=</span><span class="n">include_durations</span><span class="p">,</span>
            <span class="n">include_total_duration</span><span class="o">=</span><span class="n">include_total_duration</span><span class="p">,</span>
            <span class="n">include_removed_cases</span><span class="o">=</span><span class="n">include_removed_cases</span><span class="p">,</span>
            <span class="n">include_averages</span><span class="o">=</span><span class="n">include_averages</span><span class="p">,</span>
            <span class="n">input_config</span><span class="o">=</span><span class="n">input_config</span><span class="p">,</span>
            <span class="n">metadata_config</span><span class="o">=</span><span class="n">metadata_config</span><span class="p">,</span>
            <span class="n">output_config</span><span class="o">=</span><span class="n">output_config</span><span class="p">,</span>
            <span class="n">score_configs</span><span class="o">=</span><span class="n">score_configs</span><span class="p">,</span>
            <span class="n">label_configs</span><span class="o">=</span><span class="n">label_configs</span><span class="p">,</span>
            <span class="n">metric_configs</span><span class="o">=</span><span class="n">metric_configs</span><span class="p">,</span>
            <span class="n">duration_config</span><span class="o">=</span><span class="n">duration_config</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">Console</span><span class="p">(</span><span class="n">width</span><span class="o">=</span><span class="n">width</span><span class="p">)</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">table</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">console_table</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">baseline</span><span class="p">:</span> <span class="n">EvaluationReport</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">include_input</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">include_expected_output</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">include_output</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">include_durations</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">include_total_duration</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">include_removed_cases</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">include_averages</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">input_config</span><span class="p">:</span> <span class="n">RenderValueConfig</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">metadata_config</span><span class="p">:</span> <span class="n">RenderValueConfig</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">output_config</span><span class="p">:</span> <span class="n">RenderValueConfig</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">score_configs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RenderNumberConfig</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">label_configs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RenderValueConfig</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">metric_configs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RenderNumberConfig</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">duration_config</span><span class="p">:</span> <span class="n">RenderNumberConfig</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Table</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return a table containing the data from this report, or the diff between this report and a baseline report.</span>

<span class="sd">        Optionally include input and output details.</span>
<span class="sd">        """</span>
        <span class="n">renderer</span> <span class="o">=</span> <span class="n">EvaluationRenderer</span><span class="p">(</span>
            <span class="n">include_input</span><span class="o">=</span><span class="n">include_input</span><span class="p">,</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
            <span class="n">include_expected_output</span><span class="o">=</span><span class="n">include_expected_output</span><span class="p">,</span>
            <span class="n">include_output</span><span class="o">=</span><span class="n">include_output</span><span class="p">,</span>
            <span class="n">include_durations</span><span class="o">=</span><span class="n">include_durations</span><span class="p">,</span>
            <span class="n">include_total_duration</span><span class="o">=</span><span class="n">include_total_duration</span><span class="p">,</span>
            <span class="n">include_removed_cases</span><span class="o">=</span><span class="n">include_removed_cases</span><span class="p">,</span>
            <span class="n">include_averages</span><span class="o">=</span><span class="n">include_averages</span><span class="p">,</span>
            <span class="n">input_config</span><span class="o">=</span><span class="p">{</span><span class="o">**</span><span class="n">_DEFAULT_VALUE_CONFIG</span><span class="p">,</span> <span class="o">**</span><span class="p">(</span><span class="n">input_config</span> <span class="ow">or</span> <span class="p">{})},</span>
            <span class="n">metadata_config</span><span class="o">=</span><span class="p">{</span><span class="o">**</span><span class="n">_DEFAULT_VALUE_CONFIG</span><span class="p">,</span> <span class="o">**</span><span class="p">(</span><span class="n">metadata_config</span> <span class="ow">or</span> <span class="p">{})},</span>
            <span class="n">output_config</span><span class="o">=</span><span class="n">output_config</span> <span class="ow">or</span> <span class="n">_DEFAULT_VALUE_CONFIG</span><span class="p">,</span>
            <span class="n">score_configs</span><span class="o">=</span><span class="n">score_configs</span> <span class="ow">or</span> <span class="p">{},</span>
            <span class="n">label_configs</span><span class="o">=</span><span class="n">label_configs</span> <span class="ow">or</span> <span class="p">{},</span>
            <span class="n">metric_configs</span><span class="o">=</span><span class="n">metric_configs</span> <span class="ow">or</span> <span class="p">{},</span>
            <span class="n">duration_config</span><span class="o">=</span><span class="n">duration_config</span> <span class="ow">or</span> <span class="n">_DEFAULT_DURATION_CONFIG</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">baseline</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">renderer</span><span class="o">.</span><span class="n">build_table</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
            <span class="k">return</span> <span class="n">renderer</span><span class="o">.</span><span class="n">build_diff_table</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">baseline</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return a string representation of the report."""</span>
        <span class="n">table</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">console_table</span><span class="p">()</span>
        <span class="n">io_file</span> <span class="o">=</span> <span class="n">StringIO</span><span class="p">()</span>
        <span class="n">Console</span><span class="p">(</span><span class="n">file</span><span class="o">=</span><span class="n">io_file</span><span class="p">)</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">table</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">io_file</span><span class="o">.</span><span class="n">getvalue</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.reporting.EvaluationReport.name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code><span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The name of the report.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.reporting.EvaluationReport.cases" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">cases</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_11"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_11 > code"></button><code><span class="n">cases</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.ReportCase" href="#pydantic_evals.reporting.ReportCase">ReportCase</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The cases in the report.</p>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.reporting.EvaluationReport.print" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">print</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code><span class="nb">print</span><span class="p">(</span>
    <span class="nf">width</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">baseline</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.EvaluationReport" href="#pydantic_evals.reporting.EvaluationReport">EvaluationReport</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">include_input</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_metadata</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_expected_output</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_output</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_durations</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">include_total_duration</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_removed_cases</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_averages</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">input_config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.RenderValueConfig" href="#pydantic_evals.reporting.RenderValueConfig">RenderValueConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">metadata_config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.RenderValueConfig" href="#pydantic_evals.reporting.RenderValueConfig">RenderValueConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">output_config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.RenderValueConfig" href="#pydantic_evals.reporting.RenderValueConfig">RenderValueConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">score_configs</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.RenderNumberConfig" href="#pydantic_evals.reporting.RenderNumberConfig">RenderNumberConfig</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">label_configs</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.RenderValueConfig" href="#pydantic_evals.reporting.RenderValueConfig">RenderValueConfig</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">metric_configs</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.RenderNumberConfig" href="#pydantic_evals.reporting.RenderNumberConfig">RenderNumberConfig</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">duration_config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.RenderNumberConfig" href="#pydantic_evals.reporting.RenderNumberConfig">RenderNumberConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Print this report to the console, optionally comparing it to a baseline report.</p>
<p>If you want more control over the output, use <code>console_table</code> instead and pass it to <code>rich.Console.print</code>.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/reporting/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">156</span>
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
<span class="normal">198</span></pre></div></td><td class="code"><div><pre id="__code_13"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_13 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">print</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">width</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">baseline</span><span class="p">:</span> <span class="n">EvaluationReport</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">include_input</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_expected_output</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_output</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_durations</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">include_total_duration</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_removed_cases</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_averages</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">input_config</span><span class="p">:</span> <span class="n">RenderValueConfig</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">metadata_config</span><span class="p">:</span> <span class="n">RenderValueConfig</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">output_config</span><span class="p">:</span> <span class="n">RenderValueConfig</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">score_configs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RenderNumberConfig</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">label_configs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RenderValueConfig</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">metric_configs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RenderNumberConfig</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">duration_config</span><span class="p">:</span> <span class="n">RenderNumberConfig</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">):</span>  <span class="c1"># pragma: no cover</span>
<span class="w">    </span><span class="sd">"""Print this report to the console, optionally comparing it to a baseline report.</span>

<span class="sd">    If you want more control over the output, use `console_table` instead and pass it to `rich.Console.print`.</span>
<span class="sd">    """</span>
    <span class="n">table</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">console_table</span><span class="p">(</span>
        <span class="n">baseline</span><span class="o">=</span><span class="n">baseline</span><span class="p">,</span>
        <span class="n">include_input</span><span class="o">=</span><span class="n">include_input</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
        <span class="n">include_expected_output</span><span class="o">=</span><span class="n">include_expected_output</span><span class="p">,</span>
        <span class="n">include_output</span><span class="o">=</span><span class="n">include_output</span><span class="p">,</span>
        <span class="n">include_durations</span><span class="o">=</span><span class="n">include_durations</span><span class="p">,</span>
        <span class="n">include_total_duration</span><span class="o">=</span><span class="n">include_total_duration</span><span class="p">,</span>
        <span class="n">include_removed_cases</span><span class="o">=</span><span class="n">include_removed_cases</span><span class="p">,</span>
        <span class="n">include_averages</span><span class="o">=</span><span class="n">include_averages</span><span class="p">,</span>
        <span class="n">input_config</span><span class="o">=</span><span class="n">input_config</span><span class="p">,</span>
        <span class="n">metadata_config</span><span class="o">=</span><span class="n">metadata_config</span><span class="p">,</span>
        <span class="n">output_config</span><span class="o">=</span><span class="n">output_config</span><span class="p">,</span>
        <span class="n">score_configs</span><span class="o">=</span><span class="n">score_configs</span><span class="p">,</span>
        <span class="n">label_configs</span><span class="o">=</span><span class="n">label_configs</span><span class="p">,</span>
        <span class="n">metric_configs</span><span class="o">=</span><span class="n">metric_configs</span><span class="p">,</span>
        <span class="n">duration_config</span><span class="o">=</span><span class="n">duration_config</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">Console</span><span class="p">(</span><span class="n">width</span><span class="o">=</span><span class="n">width</span><span class="p">)</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">table</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.reporting.EvaluationReport.console_table" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">console_table</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_14"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_14 > code"></button><code><span class="nf">console_table</span><span class="p">(</span>
    <span class="n">baseline</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.EvaluationReport" href="#pydantic_evals.reporting.EvaluationReport">EvaluationReport</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">include_input</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_metadata</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_expected_output</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_output</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_durations</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">include_total_duration</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_removed_cases</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_averages</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">input_config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.RenderValueConfig" href="#pydantic_evals.reporting.RenderValueConfig">RenderValueConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">metadata_config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.RenderValueConfig" href="#pydantic_evals.reporting.RenderValueConfig">RenderValueConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">output_config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.RenderValueConfig" href="#pydantic_evals.reporting.RenderValueConfig">RenderValueConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">score_configs</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.RenderNumberConfig" href="#pydantic_evals.reporting.RenderNumberConfig">RenderNumberConfig</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">label_configs</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.RenderValueConfig" href="#pydantic_evals.reporting.RenderValueConfig">RenderValueConfig</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">metric_configs</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.RenderNumberConfig" href="#pydantic_evals.reporting.RenderNumberConfig">RenderNumberConfig</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">duration_config</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.reporting.RenderNumberConfig" href="#pydantic_evals.reporting.RenderNumberConfig">RenderNumberConfig</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="rich.table.Table" href="https://rich.readthedocs.io/en/stable/reference/table.html#rich.table.Table">Table</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return a table containing the data from this report, or the diff between this report and a baseline report.</p>
<p>Optionally include input and output details.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/reporting/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">200</span>
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
<span class="normal">243</span></pre></div></td><td class="code"><div><pre id="__code_15"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_15 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">console_table</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">baseline</span><span class="p">:</span> <span class="n">EvaluationReport</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">include_input</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_expected_output</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_output</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_durations</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">include_total_duration</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_removed_cases</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">include_averages</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">input_config</span><span class="p">:</span> <span class="n">RenderValueConfig</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">metadata_config</span><span class="p">:</span> <span class="n">RenderValueConfig</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">output_config</span><span class="p">:</span> <span class="n">RenderValueConfig</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">score_configs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RenderNumberConfig</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">label_configs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RenderValueConfig</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">metric_configs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RenderNumberConfig</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">duration_config</span><span class="p">:</span> <span class="n">RenderNumberConfig</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Table</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return a table containing the data from this report, or the diff between this report and a baseline report.</span>

<span class="sd">    Optionally include input and output details.</span>
<span class="sd">    """</span>
    <span class="n">renderer</span> <span class="o">=</span> <span class="n">EvaluationRenderer</span><span class="p">(</span>
        <span class="n">include_input</span><span class="o">=</span><span class="n">include_input</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
        <span class="n">include_expected_output</span><span class="o">=</span><span class="n">include_expected_output</span><span class="p">,</span>
        <span class="n">include_output</span><span class="o">=</span><span class="n">include_output</span><span class="p">,</span>
        <span class="n">include_durations</span><span class="o">=</span><span class="n">include_durations</span><span class="p">,</span>
        <span class="n">include_total_duration</span><span class="o">=</span><span class="n">include_total_duration</span><span class="p">,</span>
        <span class="n">include_removed_cases</span><span class="o">=</span><span class="n">include_removed_cases</span><span class="p">,</span>
        <span class="n">include_averages</span><span class="o">=</span><span class="n">include_averages</span><span class="p">,</span>
        <span class="n">input_config</span><span class="o">=</span><span class="p">{</span><span class="o">**</span><span class="n">_DEFAULT_VALUE_CONFIG</span><span class="p">,</span> <span class="o">**</span><span class="p">(</span><span class="n">input_config</span> <span class="ow">or</span> <span class="p">{})},</span>
        <span class="n">metadata_config</span><span class="o">=</span><span class="p">{</span><span class="o">**</span><span class="n">_DEFAULT_VALUE_CONFIG</span><span class="p">,</span> <span class="o">**</span><span class="p">(</span><span class="n">metadata_config</span> <span class="ow">or</span> <span class="p">{})},</span>
        <span class="n">output_config</span><span class="o">=</span><span class="n">output_config</span> <span class="ow">or</span> <span class="n">_DEFAULT_VALUE_CONFIG</span><span class="p">,</span>
        <span class="n">score_configs</span><span class="o">=</span><span class="n">score_configs</span> <span class="ow">or</span> <span class="p">{},</span>
        <span class="n">label_configs</span><span class="o">=</span><span class="n">label_configs</span> <span class="ow">or</span> <span class="p">{},</span>
        <span class="n">metric_configs</span><span class="o">=</span><span class="n">metric_configs</span> <span class="ow">or</span> <span class="p">{},</span>
        <span class="n">duration_config</span><span class="o">=</span><span class="n">duration_config</span> <span class="ow">or</span> <span class="n">_DEFAULT_DURATION_CONFIG</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">if</span> <span class="n">baseline</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">renderer</span><span class="o">.</span><span class="n">build_table</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
        <span class="k">return</span> <span class="n">renderer</span><span class="o">.</span><span class="n">build_diff_table</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">baseline</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.reporting.EvaluationReport.__str__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__str__</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_16"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_16 > code"></button><code><span class="fm">__str__</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="nf"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return a string representation of the report.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/reporting/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span></pre></div></td><td class="code"><div><pre id="__code_17"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_17 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return a string representation of the report."""</span>
    <span class="n">table</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">console_table</span><span class="p">()</span>
    <span class="n">io_file</span> <span class="o">=</span> <span class="n">StringIO</span><span class="p">()</span>
    <span class="n">Console</span><span class="p">(</span><span class="n">file</span><span class="o">=</span><span class="n">io_file</span><span class="p">)</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">table</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">io_file</span><span class="o">.</span><span class="n">getvalue</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.reporting.RenderValueConfig" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">RenderValueConfig</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing_extensions.TypedDict" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict">TypedDict</a></code></p>


        <p>A configuration for rendering a values in an Evaluation report.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/reporting/__init__.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span></pre></div></td><td class="code"><div><pre id="__code_18"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_18 > code"></button><code><span class="k">class</span><span class="w"> </span><span class="nc">RenderValueConfig</span><span class="p">(</span><span class="n">TypedDict</span><span class="p">,</span> <span class="n">total</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""A configuration for rendering a values in an Evaluation report."""</span>

    <span class="n">value_formatter</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">Any</span><span class="p">],</span> <span class="nb">str</span><span class="p">]</span>
    <span class="n">diff_checker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="nb">bool</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="n">diff_formatter</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="n">diff_style</span><span class="p">:</span> <span class="nb">str</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">





  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.reporting.RenderNumberConfig" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">RenderNumberConfig</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing_extensions.TypedDict" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict">TypedDict</a></code></p>


        <p>A configuration for rendering a particular score or metric in an Evaluation report.</p>
<p>See the implementation of <code>_RenderNumber</code> for more clarity on how these parameters affect the rendering.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/reporting/__init__.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">316</span>
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
<span class="normal">374</span></pre></div></td><td class="code"><div><pre id="__code_19"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_19 > code"></button><code tabindex="0"><span class="k">class</span><span class="w"> </span><span class="nc">RenderNumberConfig</span><span class="p">(</span><span class="n">TypedDict</span><span class="p">,</span> <span class="n">total</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""A configuration for rendering a particular score or metric in an Evaluation report.</span>

<span class="sd">    See the implementation of `_RenderNumber` for more clarity on how these parameters affect the rendering.</span>
<span class="sd">    """</span>

    <span class="n">value_formatter</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Callable</span><span class="p">[[</span><span class="nb">float</span> <span class="o">|</span> <span class="nb">int</span><span class="p">],</span> <span class="nb">str</span><span class="p">]</span>
<span class="w">    </span><span class="sd">"""The logic to use for formatting values.</span>

<span class="sd">    * If not provided, format as ints if all values are ints, otherwise at least one decimal place and at least four significant figures.</span>
<span class="sd">    * You can also use a custom string format spec, e.g. '{:.3f}'</span>
<span class="sd">    * You can also use a custom function, e.g. lambda x: f'{x:.3f}'</span>
<span class="sd">    """</span>
    <span class="n">diff_formatter</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Callable</span><span class="p">[[</span><span class="nb">float</span> <span class="o">|</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">float</span> <span class="o">|</span> <span class="nb">int</span><span class="p">],</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""The logic to use for formatting details about the diff.</span>

<span class="sd">    The strings produced by the value_formatter will always be included in the reports, but the diff_formatter is</span>
<span class="sd">    used to produce additional text about the difference between the old and new values, such as the absolute or</span>
<span class="sd">    relative difference.</span>

<span class="sd">    * If not provided, format as ints if all values are ints, otherwise at least one decimal place and at least four</span>
<span class="sd">        significant figures, and will include the percentage change.</span>
<span class="sd">    * You can also use a custom string format spec, e.g. '{:+.3f}'</span>
<span class="sd">    * You can also use a custom function, e.g. lambda x: f'{x:+.3f}'.</span>
<span class="sd">        If this function returns None, no extra diff text will be added.</span>
<span class="sd">    * You can also use None to never generate extra diff text.</span>
<span class="sd">    """</span>
    <span class="n">diff_atol</span><span class="p">:</span> <span class="nb">float</span>
<span class="w">    </span><span class="sd">"""The absolute tolerance for considering a difference "significant".</span>

<span class="sd">    A difference is "significant" if `abs(new - old) &lt; self.diff_atol + self.diff_rtol * abs(old)`.</span>

<span class="sd">    If a difference is not significant, it will not have the diff styles applied. Note that we still show</span>
<span class="sd">    both the rendered before and after values in the diff any time they differ, even if the difference is not</span>
<span class="sd">    significant. (If the rendered values are exactly the same, we only show the value once.)</span>

<span class="sd">    If not provided, use 1e-6.</span>
<span class="sd">    """</span>
    <span class="n">diff_rtol</span><span class="p">:</span> <span class="nb">float</span>
<span class="w">    </span><span class="sd">"""The relative tolerance for considering a difference "significant".</span>

<span class="sd">    See the description of `diff_atol` for more details about what makes a difference "significant".</span>

<span class="sd">    If not provided, use 0.001 if all values are ints, otherwise 0.05.</span>
<span class="sd">    """</span>
    <span class="n">diff_increase_style</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""The style to apply to diffed values that have a significant increase.</span>

<span class="sd">    See the description of `diff_atol` for more details about what makes a difference "significant".</span>

<span class="sd">    If not provided, use green for scores and red for metrics. You can also use arbitrary `rich` styles, such as "bold red".</span>
<span class="sd">    """</span>
    <span class="n">diff_decrease_style</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""The style to apply to diffed values that have significant decrease.</span>

<span class="sd">    See the description of `diff_atol` for more details about what makes a difference "significant".</span>

<span class="sd">    If not provided, use red for scores and green for metrics. You can also use arbitrary `rich` styles, such as "bold red".</span>
<span class="sd">    """</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.reporting.RenderNumberConfig.value_formatter" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">value_formatter</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_20"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_20 > code"></button><code><span class="n">value_formatter</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The logic to use for formatting values.</p>
<ul>
<li>If not provided, format as ints if all values are ints, otherwise at least one decimal place and at least four significant figures.</li>
<li>You can also use a custom string format spec, e.g. '{:.3f}'</li>
<li>You can also use a custom function, e.g. lambda x: f'{x:.3f}'</li>
</ul>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.reporting.RenderNumberConfig.diff_formatter" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">diff_formatter</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_21"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_21 > code"></button><code><span class="n">diff_formatter</span><span class="p">:</span> <span class="p">(</span>
    <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
    <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span><span class="p">]</span>
    <span class="o">|</span> <span class="kc">None</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The logic to use for formatting details about the diff.</p>
<p>The strings produced by the value_formatter will always be included in the reports, but the diff_formatter is
used to produce additional text about the difference between the old and new values, such as the absolute or
relative difference.</p>
<ul>
<li>If not provided, format as ints if all values are ints, otherwise at least one decimal place and at least four
    significant figures, and will include the percentage change.</li>
<li>You can also use a custom string format spec, e.g. '{:+.3f}'</li>
<li>You can also use a custom function, e.g. lambda x: f'{x:+.3f}'.
    If this function returns None, no extra diff text will be added.</li>
<li>You can also use None to never generate extra diff text.</li>
</ul>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.reporting.RenderNumberConfig.diff_atol" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">diff_atol</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_22"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_22 > code"></button><code><span class="n">diff_atol</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The absolute tolerance for considering a difference "significant".</p>
<p>A difference is "significant" if <code>abs(new - old) &lt; self.diff_atol + self.diff_rtol * abs(old)</code>.</p>
<p>If a difference is not significant, it will not have the diff styles applied. Note that we still show
both the rendered before and after values in the diff any time they differ, even if the difference is not
significant. (If the rendered values are exactly the same, we only show the value once.)</p>
<p>If not provided, use 1e-6.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.reporting.RenderNumberConfig.diff_rtol" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">diff_rtol</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_23"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_23 > code"></button><code><span class="n">diff_rtol</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The relative tolerance for considering a difference "significant".</p>
<p>See the description of <code>diff_atol</code> for more details about what makes a difference "significant".</p>
<p>If not provided, use 0.001 if all values are ints, otherwise 0.05.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.reporting.RenderNumberConfig.diff_increase_style" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">diff_increase_style</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_24"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_24 > code"></button><code><span class="n">diff_increase_style</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The style to apply to diffed values that have a significant increase.</p>
<p>See the description of <code>diff_atol</code> for more details about what makes a difference "significant".</p>
<p>If not provided, use green for scores and red for metrics. You can also use arbitrary <code>rich</code> styles, such as "bold red".</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.reporting.RenderNumberConfig.diff_decrease_style" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">diff_decrease_style</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_25"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_25 > code"></button><code><span class="n">diff_decrease_style</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The style to apply to diffed values that have significant decrease.</p>
<p>See the description of <code>diff_atol</code> for more details about what makes a difference "significant".</p>
<p>If not provided, use red for scores and green for metrics. You can also use arbitrary <code>rich</code> styles, such as "bold red".</p>
    </div>

</div>




  </div>

    </div>

</div>














<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.reporting.EvaluationRenderer" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">EvaluationRenderer</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>A class for rendering an EvalReport or the diff between two EvalReports.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/reporting/__init__.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 824</span>
<span class="normal"> 825</span>
<span class="normal"> 826</span>
<span class="normal"> 827</span>
<span class="normal"> 828</span>
<span class="normal"> 829</span>
<span class="normal"> 830</span>
<span class="normal"> 831</span>
<span class="normal"> 832</span>
<span class="normal"> 833</span>
<span class="normal"> 834</span>
<span class="normal"> 835</span>
<span class="normal"> 836</span>
<span class="normal"> 837</span>
<span class="normal"> 838</span>
<span class="normal"> 839</span>
<span class="normal"> 840</span>
<span class="normal"> 841</span>
<span class="normal"> 842</span>
<span class="normal"> 843</span>
<span class="normal"> 844</span>
<span class="normal"> 845</span>
<span class="normal"> 846</span>
<span class="normal"> 847</span>
<span class="normal"> 848</span>
<span class="normal"> 849</span>
<span class="normal"> 850</span>
<span class="normal"> 851</span>
<span class="normal"> 852</span>
<span class="normal"> 853</span>
<span class="normal"> 854</span>
<span class="normal"> 855</span>
<span class="normal"> 856</span>
<span class="normal"> 857</span>
<span class="normal"> 858</span>
<span class="normal"> 859</span>
<span class="normal"> 860</span>
<span class="normal"> 861</span>
<span class="normal"> 862</span>
<span class="normal"> 863</span>
<span class="normal"> 864</span>
<span class="normal"> 865</span>
<span class="normal"> 866</span>
<span class="normal"> 867</span>
<span class="normal"> 868</span>
<span class="normal"> 869</span>
<span class="normal"> 870</span>
<span class="normal"> 871</span>
<span class="normal"> 872</span>
<span class="normal"> 873</span>
<span class="normal"> 874</span>
<span class="normal"> 875</span>
<span class="normal"> 876</span>
<span class="normal"> 877</span>
<span class="normal"> 878</span>
<span class="normal"> 879</span>
<span class="normal"> 880</span>
<span class="normal"> 881</span>
<span class="normal"> 882</span>
<span class="normal"> 883</span>
<span class="normal"> 884</span>
<span class="normal"> 885</span>
<span class="normal"> 886</span>
<span class="normal"> 887</span>
<span class="normal"> 888</span>
<span class="normal"> 889</span>
<span class="normal"> 890</span>
<span class="normal"> 891</span>
<span class="normal"> 892</span>
<span class="normal"> 893</span>
<span class="normal"> 894</span>
<span class="normal"> 895</span>
<span class="normal"> 896</span>
<span class="normal"> 897</span>
<span class="normal"> 898</span>
<span class="normal"> 899</span>
<span class="normal"> 900</span>
<span class="normal"> 901</span>
<span class="normal"> 902</span>
<span class="normal"> 903</span>
<span class="normal"> 904</span>
<span class="normal"> 905</span>
<span class="normal"> 906</span>
<span class="normal"> 907</span>
<span class="normal"> 908</span>
<span class="normal"> 909</span>
<span class="normal"> 910</span>
<span class="normal"> 911</span>
<span class="normal"> 912</span>
<span class="normal"> 913</span>
<span class="normal"> 914</span>
<span class="normal"> 915</span>
<span class="normal"> 916</span>
<span class="normal"> 917</span>
<span class="normal"> 918</span>
<span class="normal"> 919</span>
<span class="normal"> 920</span>
<span class="normal"> 921</span>
<span class="normal"> 922</span>
<span class="normal"> 923</span>
<span class="normal"> 924</span>
<span class="normal"> 925</span>
<span class="normal"> 926</span>
<span class="normal"> 927</span>
<span class="normal"> 928</span>
<span class="normal"> 929</span>
<span class="normal"> 930</span>
<span class="normal"> 931</span>
<span class="normal"> 932</span>
<span class="normal"> 933</span>
<span class="normal"> 934</span>
<span class="normal"> 935</span>
<span class="normal"> 936</span>
<span class="normal"> 937</span>
<span class="normal"> 938</span>
<span class="normal"> 939</span>
<span class="normal"> 940</span>
<span class="normal"> 941</span>
<span class="normal"> 942</span>
<span class="normal"> 943</span>
<span class="normal"> 944</span>
<span class="normal"> 945</span>
<span class="normal"> 946</span>
<span class="normal"> 947</span>
<span class="normal"> 948</span>
<span class="normal"> 949</span>
<span class="normal"> 950</span>
<span class="normal"> 951</span>
<span class="normal"> 952</span>
<span class="normal"> 953</span>
<span class="normal"> 954</span>
<span class="normal"> 955</span>
<span class="normal"> 956</span>
<span class="normal"> 957</span>
<span class="normal"> 958</span>
<span class="normal"> 959</span>
<span class="normal"> 960</span>
<span class="normal"> 961</span>
<span class="normal"> 962</span>
<span class="normal"> 963</span>
<span class="normal"> 964</span>
<span class="normal"> 965</span>
<span class="normal"> 966</span>
<span class="normal"> 967</span>
<span class="normal"> 968</span>
<span class="normal"> 969</span>
<span class="normal"> 970</span>
<span class="normal"> 971</span>
<span class="normal"> 972</span>
<span class="normal"> 973</span>
<span class="normal"> 974</span>
<span class="normal"> 975</span>
<span class="normal"> 976</span>
<span class="normal"> 977</span>
<span class="normal"> 978</span>
<span class="normal"> 979</span>
<span class="normal"> 980</span>
<span class="normal"> 981</span>
<span class="normal"> 982</span>
<span class="normal"> 983</span>
<span class="normal"> 984</span>
<span class="normal"> 985</span>
<span class="normal"> 986</span>
<span class="normal"> 987</span>
<span class="normal"> 988</span>
<span class="normal"> 989</span>
<span class="normal"> 990</span>
<span class="normal"> 991</span>
<span class="normal"> 992</span>
<span class="normal"> 993</span>
<span class="normal"> 994</span>
<span class="normal"> 995</span>
<span class="normal"> 996</span>
<span class="normal"> 997</span>
<span class="normal"> 998</span>
<span class="normal"> 999</span>
<span class="normal">1000</span>
<span class="normal">1001</span>
<span class="normal">1002</span>
<span class="normal">1003</span>
<span class="normal">1004</span>
<span class="normal">1005</span>
<span class="normal">1006</span>
<span class="normal">1007</span>
<span class="normal">1008</span>
<span class="normal">1009</span>
<span class="normal">1010</span>
<span class="normal">1011</span>
<span class="normal">1012</span>
<span class="normal">1013</span>
<span class="normal">1014</span>
<span class="normal">1015</span>
<span class="normal">1016</span>
<span class="normal">1017</span></pre></div></td><td class="code"><div><pre id="__code_26"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_26 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">EvaluationRenderer</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""A class for rendering an EvalReport or the diff between two EvalReports."""</span>

    <span class="c1"># Columns to include</span>
    <span class="n">include_input</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">include_expected_output</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">include_output</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">include_durations</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">include_total_duration</span><span class="p">:</span> <span class="nb">bool</span>

    <span class="c1"># Rows to include</span>
    <span class="n">include_removed_cases</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">include_averages</span><span class="p">:</span> <span class="nb">bool</span>

    <span class="n">input_config</span><span class="p">:</span> <span class="n">RenderValueConfig</span>
    <span class="n">metadata_config</span><span class="p">:</span> <span class="n">RenderValueConfig</span>
    <span class="n">output_config</span><span class="p">:</span> <span class="n">RenderValueConfig</span>
    <span class="n">score_configs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RenderNumberConfig</span><span class="p">]</span>
    <span class="n">label_configs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RenderValueConfig</span><span class="p">]</span>
    <span class="n">metric_configs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">RenderNumberConfig</span><span class="p">]</span>
    <span class="n">duration_config</span><span class="p">:</span> <span class="n">RenderNumberConfig</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">include_scores</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">report</span><span class="p">:</span> <span class="n">EvaluationReport</span><span class="p">,</span> <span class="n">baseline</span><span class="p">:</span> <span class="n">EvaluationReport</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
        <span class="k">return</span> <span class="nb">any</span><span class="p">(</span><span class="n">case</span><span class="o">.</span><span class="n">scores</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_all_cases</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">))</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">include_labels</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">report</span><span class="p">:</span> <span class="n">EvaluationReport</span><span class="p">,</span> <span class="n">baseline</span><span class="p">:</span> <span class="n">EvaluationReport</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
        <span class="k">return</span> <span class="nb">any</span><span class="p">(</span><span class="n">case</span><span class="o">.</span><span class="n">labels</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_all_cases</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">))</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">include_metrics</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">report</span><span class="p">:</span> <span class="n">EvaluationReport</span><span class="p">,</span> <span class="n">baseline</span><span class="p">:</span> <span class="n">EvaluationReport</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
        <span class="k">return</span> <span class="nb">any</span><span class="p">(</span><span class="n">case</span><span class="o">.</span><span class="n">metrics</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_all_cases</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">))</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">include_assertions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">report</span><span class="p">:</span> <span class="n">EvaluationReport</span><span class="p">,</span> <span class="n">baseline</span><span class="p">:</span> <span class="n">EvaluationReport</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
        <span class="k">return</span> <span class="nb">any</span><span class="p">(</span><span class="n">case</span><span class="o">.</span><span class="n">assertions</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_all_cases</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">))</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_all_cases</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">report</span><span class="p">:</span> <span class="n">EvaluationReport</span><span class="p">,</span> <span class="n">baseline</span><span class="p">:</span> <span class="n">EvaluationReport</span> <span class="o">|</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">ReportCase</span><span class="p">]:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">baseline</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">report</span><span class="o">.</span><span class="n">cases</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">report</span><span class="o">.</span><span class="n">cases</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_baseline_cases_to_include</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_baseline_cases_to_include</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">report</span><span class="p">:</span> <span class="n">EvaluationReport</span><span class="p">,</span> <span class="n">baseline</span><span class="p">:</span> <span class="n">EvaluationReport</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">ReportCase</span><span class="p">]:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">include_removed_cases</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">baseline</span><span class="o">.</span><span class="n">cases</span>
        <span class="n">report_case_names</span> <span class="o">=</span> <span class="p">{</span><span class="n">case</span><span class="o">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">report</span><span class="o">.</span><span class="n">cases</span><span class="p">}</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">case</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">baseline</span><span class="o">.</span><span class="n">cases</span> <span class="k">if</span> <span class="n">case</span><span class="o">.</span><span class="n">name</span> <span class="ow">in</span> <span class="n">report_case_names</span><span class="p">]</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_get_case_renderer</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">report</span><span class="p">:</span> <span class="n">EvaluationReport</span><span class="p">,</span> <span class="n">baseline</span><span class="p">:</span> <span class="n">EvaluationReport</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ReportCaseRenderer</span><span class="p">:</span>
        <span class="n">input_renderer</span> <span class="o">=</span> <span class="n">_ValueRenderer</span><span class="o">.</span><span class="n">from_config</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">input_config</span><span class="p">)</span>
        <span class="n">metadata_renderer</span> <span class="o">=</span> <span class="n">_ValueRenderer</span><span class="o">.</span><span class="n">from_config</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata_config</span><span class="p">)</span>
        <span class="n">output_renderer</span> <span class="o">=</span> <span class="n">_ValueRenderer</span><span class="o">.</span><span class="n">from_config</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">output_config</span><span class="p">)</span>
        <span class="n">score_renderers</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_infer_score_renderers</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">)</span>
        <span class="n">label_renderers</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_infer_label_renderers</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">)</span>
        <span class="n">metric_renderers</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_infer_metric_renderers</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">)</span>
        <span class="n">duration_renderer</span> <span class="o">=</span> <span class="n">_NumberRenderer</span><span class="o">.</span><span class="n">infer_from_config</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">duration_config</span><span class="p">,</span> <span class="s1">'duration'</span><span class="p">,</span> <span class="p">[</span><span class="n">x</span><span class="o">.</span><span class="n">task_duration</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_all_cases</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">)]</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">ReportCaseRenderer</span><span class="p">(</span>
            <span class="n">include_input</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">include_input</span><span class="p">,</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">include_metadata</span><span class="p">,</span>
            <span class="n">include_expected_output</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">include_expected_output</span><span class="p">,</span>
            <span class="n">include_output</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">include_output</span><span class="p">,</span>
            <span class="n">include_scores</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">include_scores</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">),</span>
            <span class="n">include_labels</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">include_labels</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">),</span>
            <span class="n">include_metrics</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">include_metrics</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">),</span>
            <span class="n">include_assertions</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">include_assertions</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">),</span>
            <span class="n">include_durations</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">include_durations</span><span class="p">,</span>
            <span class="n">include_total_duration</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">include_total_duration</span><span class="p">,</span>
            <span class="n">input_renderer</span><span class="o">=</span><span class="n">input_renderer</span><span class="p">,</span>
            <span class="n">metadata_renderer</span><span class="o">=</span><span class="n">metadata_renderer</span><span class="p">,</span>
            <span class="n">output_renderer</span><span class="o">=</span><span class="n">output_renderer</span><span class="p">,</span>
            <span class="n">score_renderers</span><span class="o">=</span><span class="n">score_renderers</span><span class="p">,</span>
            <span class="n">label_renderers</span><span class="o">=</span><span class="n">label_renderers</span><span class="p">,</span>
            <span class="n">metric_renderers</span><span class="o">=</span><span class="n">metric_renderers</span><span class="p">,</span>
            <span class="n">duration_renderer</span><span class="o">=</span><span class="n">duration_renderer</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">build_table</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">report</span><span class="p">:</span> <span class="n">EvaluationReport</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Table</span><span class="p">:</span>
        <span class="n">case_renderer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_case_renderer</span><span class="p">(</span><span class="n">report</span><span class="p">)</span>
        <span class="n">table</span> <span class="o">=</span> <span class="n">case_renderer</span><span class="o">.</span><span class="n">build_base_table</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Evaluation Summary: </span><span class="si">{</span><span class="n">report</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">report</span><span class="o">.</span><span class="n">cases</span><span class="p">:</span>
            <span class="n">table</span><span class="o">.</span><span class="n">add_row</span><span class="p">(</span><span class="o">*</span><span class="n">case_renderer</span><span class="o">.</span><span class="n">build_row</span><span class="p">(</span><span class="n">case</span><span class="p">))</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">include_averages</span><span class="p">:</span>
            <span class="n">average</span> <span class="o">=</span> <span class="n">report</span><span class="o">.</span><span class="n">averages</span><span class="p">()</span>
            <span class="n">table</span><span class="o">.</span><span class="n">add_row</span><span class="p">(</span><span class="o">*</span><span class="n">case_renderer</span><span class="o">.</span><span class="n">build_aggregate_row</span><span class="p">(</span><span class="n">average</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">table</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">build_diff_table</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">report</span><span class="p">:</span> <span class="n">EvaluationReport</span><span class="p">,</span> <span class="n">baseline</span><span class="p">:</span> <span class="n">EvaluationReport</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Table</span><span class="p">:</span>
        <span class="n">report_cases</span> <span class="o">=</span> <span class="n">report</span><span class="o">.</span><span class="n">cases</span>
        <span class="n">baseline_cases</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_baseline_cases_to_include</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">)</span>

        <span class="n">report_cases_by_id</span> <span class="o">=</span> <span class="p">{</span><span class="n">case</span><span class="o">.</span><span class="n">name</span><span class="p">:</span> <span class="n">case</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">report_cases</span><span class="p">}</span>
        <span class="n">baseline_cases_by_id</span> <span class="o">=</span> <span class="p">{</span><span class="n">case</span><span class="o">.</span><span class="n">name</span><span class="p">:</span> <span class="n">case</span> <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">baseline_cases</span><span class="p">}</span>

        <span class="n">diff_cases</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">tuple</span><span class="p">[</span><span class="n">ReportCase</span><span class="p">,</span> <span class="n">ReportCase</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">removed_cases</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ReportCase</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">added_cases</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ReportCase</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">case_id</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">baseline_cases_by_id</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span> <span class="o">|</span> <span class="nb">set</span><span class="p">(</span><span class="n">report_cases_by_id</span><span class="o">.</span><span class="n">keys</span><span class="p">())):</span>
            <span class="n">maybe_baseline_case</span> <span class="o">=</span> <span class="n">baseline_cases_by_id</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">case_id</span><span class="p">)</span>
            <span class="n">maybe_report_case</span> <span class="o">=</span> <span class="n">report_cases_by_id</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">case_id</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">maybe_baseline_case</span> <span class="ow">and</span> <span class="n">maybe_report_case</span><span class="p">:</span>
                <span class="n">diff_cases</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">maybe_baseline_case</span><span class="p">,</span> <span class="n">maybe_report_case</span><span class="p">))</span>
            <span class="k">elif</span> <span class="n">maybe_baseline_case</span><span class="p">:</span>
                <span class="n">removed_cases</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">maybe_baseline_case</span><span class="p">)</span>
            <span class="k">elif</span> <span class="n">maybe_report_case</span><span class="p">:</span>
                <span class="n">added_cases</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">maybe_report_case</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
                <span class="k">assert</span> <span class="kc">False</span><span class="p">,</span> <span class="s1">'This should be unreachable'</span>

        <span class="n">case_renderer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_case_renderer</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">)</span>
        <span class="n">diff_name</span> <span class="o">=</span> <span class="n">baseline</span><span class="o">.</span><span class="n">name</span> <span class="k">if</span> <span class="n">baseline</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="n">report</span><span class="o">.</span><span class="n">name</span> <span class="k">else</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">baseline</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s1"> → </span><span class="si">{</span><span class="n">report</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s1">'</span>
        <span class="n">table</span> <span class="o">=</span> <span class="n">case_renderer</span><span class="o">.</span><span class="n">build_base_table</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Evaluation Diff: </span><span class="si">{</span><span class="n">diff_name</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">baseline_case</span><span class="p">,</span> <span class="n">new_case</span> <span class="ow">in</span> <span class="n">diff_cases</span><span class="p">:</span>
            <span class="n">table</span><span class="o">.</span><span class="n">add_row</span><span class="p">(</span><span class="o">*</span><span class="n">case_renderer</span><span class="o">.</span><span class="n">build_diff_row</span><span class="p">(</span><span class="n">new_case</span><span class="p">,</span> <span class="n">baseline_case</span><span class="p">))</span>
        <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">added_cases</span><span class="p">:</span>
            <span class="n">row</span> <span class="o">=</span> <span class="n">case_renderer</span><span class="o">.</span><span class="n">build_row</span><span class="p">(</span><span class="n">case</span><span class="p">)</span>
            <span class="n">row</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'[green]+ Added Case[/]</span><span class="se">\n</span><span class="si">{</span><span class="n">row</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="si">}</span><span class="s1">'</span>
            <span class="n">table</span><span class="o">.</span><span class="n">add_row</span><span class="p">(</span><span class="o">*</span><span class="n">row</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">removed_cases</span><span class="p">:</span>
            <span class="n">row</span> <span class="o">=</span> <span class="n">case_renderer</span><span class="o">.</span><span class="n">build_row</span><span class="p">(</span><span class="n">case</span><span class="p">)</span>
            <span class="n">row</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'[red]- Removed Case[/]</span><span class="se">\n</span><span class="si">{</span><span class="n">row</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="si">}</span><span class="s1">'</span>
            <span class="n">table</span><span class="o">.</span><span class="n">add_row</span><span class="p">(</span><span class="o">*</span><span class="n">row</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">include_averages</span><span class="p">:</span>
            <span class="n">report_average</span> <span class="o">=</span> <span class="n">ReportCaseAggregate</span><span class="o">.</span><span class="n">average</span><span class="p">(</span><span class="n">report_cases</span><span class="p">)</span>
            <span class="n">baseline_average</span> <span class="o">=</span> <span class="n">ReportCaseAggregate</span><span class="o">.</span><span class="n">average</span><span class="p">(</span><span class="n">baseline_cases</span><span class="p">)</span>
            <span class="n">table</span><span class="o">.</span><span class="n">add_row</span><span class="p">(</span><span class="o">*</span><span class="n">case_renderer</span><span class="o">.</span><span class="n">build_diff_aggregate_row</span><span class="p">(</span><span class="n">report_average</span><span class="p">,</span> <span class="n">baseline_average</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">table</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_infer_score_renderers</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">report</span><span class="p">:</span> <span class="n">EvaluationReport</span><span class="p">,</span> <span class="n">baseline</span><span class="p">:</span> <span class="n">EvaluationReport</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">_NumberRenderer</span><span class="p">]:</span>
        <span class="n">all_cases</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_all_cases</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">)</span>

        <span class="n">values_by_name</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">list</span><span class="p">[</span><span class="nb">float</span> <span class="o">|</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">all_cases</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">score</span> <span class="ow">in</span> <span class="n">case</span><span class="o">.</span><span class="n">scores</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="n">values_by_name</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="n">k</span><span class="p">,</span> <span class="p">[])</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">score</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>

        <span class="n">all_renderers</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">_NumberRenderer</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">values</span> <span class="ow">in</span> <span class="n">values_by_name</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="n">merged_config</span> <span class="o">=</span> <span class="n">_DEFAULT_NUMBER_CONFIG</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
            <span class="n">merged_config</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">score_configs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="p">{}))</span>
            <span class="n">all_renderers</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">_NumberRenderer</span><span class="o">.</span><span class="n">infer_from_config</span><span class="p">(</span><span class="n">merged_config</span><span class="p">,</span> <span class="s1">'score'</span><span class="p">,</span> <span class="n">values</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">all_renderers</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_infer_label_renderers</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">report</span><span class="p">:</span> <span class="n">EvaluationReport</span><span class="p">,</span> <span class="n">baseline</span><span class="p">:</span> <span class="n">EvaluationReport</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">_ValueRenderer</span><span class="p">]:</span>
        <span class="n">all_cases</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_all_cases</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">)</span>
        <span class="n">all_names</span><span class="p">:</span> <span class="nb">set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">all_cases</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">k</span> <span class="ow">in</span> <span class="n">case</span><span class="o">.</span><span class="n">labels</span><span class="p">:</span>
                <span class="n">all_names</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">k</span><span class="p">)</span>

        <span class="n">all_renderers</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">_ValueRenderer</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">all_names</span><span class="p">:</span>
            <span class="n">merged_config</span> <span class="o">=</span> <span class="n">_DEFAULT_VALUE_CONFIG</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
            <span class="n">merged_config</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">label_configs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="p">{}))</span>
            <span class="n">all_renderers</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">_ValueRenderer</span><span class="o">.</span><span class="n">from_config</span><span class="p">(</span><span class="n">merged_config</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">all_renderers</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_infer_metric_renderers</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">report</span><span class="p">:</span> <span class="n">EvaluationReport</span><span class="p">,</span> <span class="n">baseline</span><span class="p">:</span> <span class="n">EvaluationReport</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">_NumberRenderer</span><span class="p">]:</span>
        <span class="n">all_cases</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_all_cases</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">)</span>

        <span class="n">values_by_name</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">list</span><span class="p">[</span><span class="nb">float</span> <span class="o">|</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">case</span> <span class="ow">in</span> <span class="n">all_cases</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">case</span><span class="o">.</span><span class="n">metrics</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="n">values_by_name</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="n">k</span><span class="p">,</span> <span class="p">[])</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">v</span><span class="p">)</span>

        <span class="n">all_renderers</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">_NumberRenderer</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">values</span> <span class="ow">in</span> <span class="n">values_by_name</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="n">merged_config</span> <span class="o">=</span> <span class="n">_DEFAULT_NUMBER_CONFIG</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
            <span class="n">merged_config</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">metric_configs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="p">{}))</span>
            <span class="n">all_renderers</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">_NumberRenderer</span><span class="o">.</span><span class="n">infer_from_config</span><span class="p">(</span><span class="n">merged_config</span><span class="p">,</span> <span class="s1">'metric'</span><span class="p">,</span> <span class="n">values</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">all_renderers</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_infer_duration_renderer</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">report</span><span class="p">:</span> <span class="n">EvaluationReport</span><span class="p">,</span> <span class="n">baseline</span><span class="p">:</span> <span class="n">EvaluationReport</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_NumberRenderer</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
        <span class="n">all_cases</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_all_cases</span><span class="p">(</span><span class="n">report</span><span class="p">,</span> <span class="n">baseline</span><span class="p">)</span>
        <span class="n">all_durations</span> <span class="o">=</span> <span class="p">[</span><span class="n">x</span><span class="o">.</span><span class="n">task_duration</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">all_cases</span><span class="p">]</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">include_total_duration</span><span class="p">:</span>
            <span class="n">all_durations</span> <span class="o">+=</span> <span class="p">[</span><span class="n">x</span><span class="o">.</span><span class="n">total_duration</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">all_cases</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">_NumberRenderer</span><span class="o">.</span><span class="n">infer_from_config</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">duration_config</span><span class="p">,</span> <span class="s1">'duration'</span><span class="p">,</span> <span class="n">all_durations</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">





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