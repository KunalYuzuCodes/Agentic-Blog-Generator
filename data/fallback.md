<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/api/models/fallback/">
      
      
        <link rel="prev" href="../function/">
      
      
        <link rel="next" href="../wrapper/">
      
      
      <link rel="icon" href="../../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>pydantic_ai.models.fallback - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="pydantic_ai.models.fallback - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/api/models/fallback.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/api/models/fallback/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="pydantic_ai.models.fallback - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/api/models/fallback.png">
      
    
    
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
      
        
        <a href="#pydantic_aimodelsfallback" class="md-skip">
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
            
              pydantic_ai.models.fallback
            
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
      <a href="../base/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../openai/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.openai
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../anthropic/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.anthropic
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../bedrock/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.bedrock
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../cohere/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.cohere
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../gemini/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.gemini
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../groq/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.groq
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../instrumented/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mistral/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.test
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../function/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.fallback" class="md-nav__link">
    <span class="md-ellipsis">
      fallback
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.fallback.FallbackModel" class="md-nav__link">
    <span class="md-ellipsis">
      FallbackModel
    </span>
  </a>
  
    <nav class="md-nav" aria-label="FallbackModel">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.fallback.FallbackModel.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.fallback.FallbackModel.request" class="md-nav__link">
    <span class="md-ellipsis">
      request
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.fallback.FallbackModel.request_stream" class="md-nav__link">
    <span class="md-ellipsis">
      request_stream
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.fallback.FallbackModel.model_name" class="md-nav__link">
    <span class="md-ellipsis">
      model_name
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
      <a href="../wrapper/" class="md-nav__link">
        
  
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
      <a href="../../pydantic_evals/dataset/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/evaluators/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/generation/" class="md-nav__link">
        
  
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
  <a href="#pydantic_ai.models.fallback" class="md-nav__link">
    <span class="md-ellipsis">
      fallback
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.fallback.FallbackModel" class="md-nav__link">
    <span class="md-ellipsis">
      FallbackModel
    </span>
  </a>
  
    <nav class="md-nav" aria-label="FallbackModel">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.fallback.FallbackModel.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.fallback.FallbackModel.request" class="md-nav__link">
    <span class="md-ellipsis">
      request
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.fallback.FallbackModel.request_stream" class="md-nav__link">
    <span class="md-ellipsis">
      request_stream
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.fallback.FallbackModel.model_name" class="md-nav__link">
    <span class="md-ellipsis">
      model_name
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
                
                  


  
  


<h1 id="pydantic_aimodelsfallback">pydantic_ai.models.fallback</h1>


<div class="doc doc-object doc-module">



<a id="pydantic_ai.models.fallback"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">























































<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.models.fallback.FallbackModel" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">FallbackModel</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../base/#pydantic_ai.models.Model">Model</a></code></p>


        <p>A model that uses one or more fallback models upon failure.</p>
<p>Apart from <code>__init__</code>, all methods are private or match those of the base class.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/fallback.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 21</span>
<span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
<span class="normal"> 38</span>
<span class="normal"> 39</span>
<span class="normal"> 40</span>
<span class="normal"> 41</span>
<span class="normal"> 42</span>
<span class="normal"> 43</span>
<span class="normal"> 44</span>
<span class="normal"> 45</span>
<span class="normal"> 46</span>
<span class="normal"> 47</span>
<span class="normal"> 48</span>
<span class="normal"> 49</span>
<span class="normal"> 50</span>
<span class="normal"> 51</span>
<span class="normal"> 52</span>
<span class="normal"> 53</span>
<span class="normal"> 54</span>
<span class="normal"> 55</span>
<span class="normal"> 56</span>
<span class="normal"> 57</span>
<span class="normal"> 58</span>
<span class="normal"> 59</span>
<span class="normal"> 60</span>
<span class="normal"> 61</span>
<span class="normal"> 62</span>
<span class="normal"> 63</span>
<span class="normal"> 64</span>
<span class="normal"> 65</span>
<span class="normal"> 66</span>
<span class="normal"> 67</span>
<span class="normal"> 68</span>
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
<span class="normal">126</span></pre></div></td><td class="code"><div><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="nd">@dataclass</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="k">class</span><span class="w"> </span><span class="nc">FallbackModel</span><span class="p">(</span><span class="n">Model</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""A model that uses one or more fallback models upon failure.</span>

<span class="sd">    Apart from `__init__`, all methods are private or match those of the base class.</span>
<span class="sd">    """</span>

    <span class="n">models</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Model</span><span class="p">]</span>

    <span class="n">_model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_fallback_on</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="ne">Exception</span><span class="p">],</span> <span class="nb">bool</span><span class="p">]</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">default_model</span><span class="p">:</span> <span class="n">Model</span> <span class="o">|</span> <span class="n">KnownModelName</span><span class="p">,</span>
        <span class="o">*</span><span class="n">fallback_models</span><span class="p">:</span> <span class="n">Model</span> <span class="o">|</span> <span class="n">KnownModelName</span><span class="p">,</span>
        <span class="n">fallback_on</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="ne">Exception</span><span class="p">],</span> <span class="nb">bool</span><span class="p">]</span> <span class="o">|</span> <span class="nb">tuple</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="ne">Exception</span><span class="p">],</span> <span class="o">...</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">ModelHTTPError</span><span class="p">,),</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize a fallback model instance.</span>

<span class="sd">        Args:</span>
<span class="sd">            default_model: The name or instance of the default model to use.</span>
<span class="sd">            fallback_models: The names or instances of the fallback models to use upon failure.</span>
<span class="sd">            fallback_on: A callable or tuple of exceptions that should trigger a fallback.</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">models</span> <span class="o">=</span> <span class="p">[</span><span class="n">infer_model</span><span class="p">(</span><span class="n">default_model</span><span class="p">),</span> <span class="o">*</span><span class="p">[</span><span class="n">infer_model</span><span class="p">(</span><span class="n">m</span><span class="p">)</span> <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="n">fallback_models</span><span class="p">]]</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">fallback_on</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_fallback_on</span> <span class="o">=</span> <span class="n">_default_fallback_condition_factory</span><span class="p">(</span><span class="n">fallback_on</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_fallback_on</span> <span class="o">=</span> <span class="n">fallback_on</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">request</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">tuple</span><span class="p">[</span><span class="n">ModelResponse</span><span class="p">,</span> <span class="n">Usage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Try each model in sequence until one succeeds.</span>

<span class="sd">        In case of failure, raise a FallbackExceptionGroup with all exceptions.</span>
<span class="sd">        """</span>
        <span class="n">exceptions</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">models</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">response</span><span class="p">,</span> <span class="n">usage</span> <span class="o">=</span> <span class="k">await</span> <span class="n">model</span><span class="o">.</span><span class="n">request</span><span class="p">(</span><span class="n">messages</span><span class="p">,</span> <span class="n">model_settings</span><span class="p">,</span> <span class="n">model_request_parameters</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">exc</span><span class="p">:</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fallback_on</span><span class="p">(</span><span class="n">exc</span><span class="p">):</span>
                    <span class="n">exceptions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">exc</span><span class="p">)</span>
                    <span class="k">continue</span>
                <span class="k">raise</span> <span class="n">exc</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">_set_span_attributes</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">response</span><span class="p">,</span> <span class="n">usage</span>

        <span class="k">raise</span> <span class="n">FallbackExceptionGroup</span><span class="p">(</span><span class="s1">'All models from FallbackModel failed'</span><span class="p">,</span> <span class="n">exceptions</span><span class="p">)</span>

    <span class="nd">@asynccontextmanager</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">request_stream</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">StreamedResponse</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Try each model in sequence until one succeeds."""</span>
        <span class="n">exceptions</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">models</span><span class="p">:</span>
            <span class="k">async</span> <span class="k">with</span> <span class="n">AsyncExitStack</span><span class="p">()</span> <span class="k">as</span> <span class="n">stack</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">stack</span><span class="o">.</span><span class="n">enter_async_context</span><span class="p">(</span>
                        <span class="n">model</span><span class="o">.</span><span class="n">request_stream</span><span class="p">(</span><span class="n">messages</span><span class="p">,</span> <span class="n">model_settings</span><span class="p">,</span> <span class="n">model_request_parameters</span><span class="p">)</span>
                    <span class="p">)</span>
                <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">exc</span><span class="p">:</span>
                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fallback_on</span><span class="p">(</span><span class="n">exc</span><span class="p">):</span>
                        <span class="n">exceptions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">exc</span><span class="p">)</span>
                        <span class="k">continue</span>
                    <span class="k">raise</span> <span class="n">exc</span>

                <span class="bp">self</span><span class="o">.</span><span class="n">_set_span_attributes</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
                <span class="k">yield</span> <span class="n">response</span>
                <span class="k">return</span>

        <span class="k">raise</span> <span class="n">FallbackExceptionGroup</span><span class="p">(</span><span class="s1">'All models from FallbackModel failed'</span><span class="p">,</span> <span class="n">exceptions</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_set_span_attributes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">model</span><span class="p">:</span> <span class="n">Model</span><span class="p">):</span>
        <span class="k">with</span> <span class="n">suppress</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
            <span class="n">span</span> <span class="o">=</span> <span class="n">get_current_span</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">span</span><span class="o">.</span><span class="n">is_recording</span><span class="p">():</span>
                <span class="n">attributes</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">span</span><span class="p">,</span> <span class="s1">'attributes'</span><span class="p">,</span> <span class="p">{})</span>
                <span class="k">if</span> <span class="n">attributes</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'gen_ai.request.model'</span><span class="p">)</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">model_name</span><span class="p">:</span>
                    <span class="n">span</span><span class="o">.</span><span class="n">set_attributes</span><span class="p">(</span><span class="n">InstrumentedModel</span><span class="o">.</span><span class="n">model_attributes</span><span class="p">(</span><span class="n">model</span><span class="p">))</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">model_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""The model name."""</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s1">'fallback:</span><span class="si">{</span><span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">model_name</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">model</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="bp">self</span><span class="o">.</span><span class="n">models</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">system</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s1">'fallback:</span><span class="si">{</span><span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">system</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">model</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="bp">self</span><span class="o">.</span><span class="n">models</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">base_url</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">models</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">base_url</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.models.fallback.FallbackModel.__init__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__init__</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="nf">default_model</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../base/#pydantic_ai.models.Model">Model</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../base/#pydantic_ai.models.KnownModelName">KnownModelName</a></span><span class="p">,</span>
    <span class="o">*</span><span class="n">fallback_models</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../base/#pydantic_ai.models.Model">Model</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../base/#pydantic_ai.models.KnownModelName">KnownModelName</a></span><span class="p">,</span>
    <span class="n">fallback_on</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#Exception">Exception</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span><span class="p">]</span>
        <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple">tuple</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#Exception">Exception</a></span><span class="p">],</span> <span class="o">...</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">=</span> <span class="p">(</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.exceptions.ModelHTTPError" href="../../exceptions/#pydantic_ai.exceptions.ModelHTTPError">ModelHTTPError</a></span><span class="p">,)</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Initialize a fallback model instance.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>default_model</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../base/#pydantic_ai.models.Model">Model</a> | <a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../base/#pydantic_ai.models.KnownModelName">KnownModelName</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The name or instance of the default model to use.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>fallback_models</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../base/#pydantic_ai.models.Model">Model</a> | <a class="autorefs autorefs-internal" title="pydantic_ai.models.KnownModelName" href="../base/#pydantic_ai.models.KnownModelName">KnownModelName</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The names or instances of the fallback models to use upon failure.</p>
              </div>
            </td>
            <td>
                  <code>()</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>fallback_on</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a>[[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#Exception">Exception</a>], <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a>] | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple">tuple</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#Exception">Exception</a>], ...]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>A callable or tuple of exceptions that should trigger a fallback.</p>
              </div>
            </td>
            <td>
                  <code>(<a class="autorefs autorefs-internal" title="pydantic_ai.exceptions.ModelHTTPError" href="../../exceptions/#pydantic_ai.exceptions.ModelHTTPError">ModelHTTPError</a>,)</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/fallback.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">33</span>
<span class="normal">34</span>
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
<span class="normal">51</span></pre></div></td><td class="code"><div><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">default_model</span><span class="p">:</span> <span class="n">Model</span> <span class="o">|</span> <span class="n">KnownModelName</span><span class="p">,</span>
    <span class="o">*</span><span class="n">fallback_models</span><span class="p">:</span> <span class="n">Model</span> <span class="o">|</span> <span class="n">KnownModelName</span><span class="p">,</span>
    <span class="n">fallback_on</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[</span><span class="ne">Exception</span><span class="p">],</span> <span class="nb">bool</span><span class="p">]</span> <span class="o">|</span> <span class="nb">tuple</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="ne">Exception</span><span class="p">],</span> <span class="o">...</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">ModelHTTPError</span><span class="p">,),</span>
<span class="p">):</span>
<span class="w">    </span><span class="sd">"""Initialize a fallback model instance.</span>

<span class="sd">    Args:</span>
<span class="sd">        default_model: The name or instance of the default model to use.</span>
<span class="sd">        fallback_models: The names or instances of the fallback models to use upon failure.</span>
<span class="sd">        fallback_on: A callable or tuple of exceptions that should trigger a fallback.</span>
<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">models</span> <span class="o">=</span> <span class="p">[</span><span class="n">infer_model</span><span class="p">(</span><span class="n">default_model</span><span class="p">),</span> <span class="o">*</span><span class="p">[</span><span class="n">infer_model</span><span class="p">(</span><span class="n">m</span><span class="p">)</span> <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="n">fallback_models</span><span class="p">]]</span>

    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">fallback_on</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_fallback_on</span> <span class="o">=</span> <span class="n">_default_fallback_condition_factory</span><span class="p">(</span><span class="n">fallback_on</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_fallback_on</span> <span class="o">=</span> <span class="n">fallback_on</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.models.fallback.FallbackModel.request" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">request</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code><span class="nf">request</span><span class="p">(</span>
    <span class="n">messages</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">],</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.ModelRequestParameters" href="../base/#pydantic_ai.models.ModelRequestParameters">ModelRequestParameters</a></span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple">tuple</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponse" href="../../messages/#pydantic_ai.messages.ModelResponse">ModelResponse</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../../usage/#pydantic_ai.usage.Usage">Usage</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Try each model in sequence until one succeeds.</p>
<p>In case of failure, raise a FallbackExceptionGroup with all exceptions.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/fallback.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">53</span>
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
<span class="normal">77</span></pre></div></td><td class="code"><div><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">request</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">tuple</span><span class="p">[</span><span class="n">ModelResponse</span><span class="p">,</span> <span class="n">Usage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Try each model in sequence until one succeeds.</span>

<span class="sd">    In case of failure, raise a FallbackExceptionGroup with all exceptions.</span>
<span class="sd">    """</span>
    <span class="n">exceptions</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">for</span> <span class="n">model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">models</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">response</span><span class="p">,</span> <span class="n">usage</span> <span class="o">=</span> <span class="k">await</span> <span class="n">model</span><span class="o">.</span><span class="n">request</span><span class="p">(</span><span class="n">messages</span><span class="p">,</span> <span class="n">model_settings</span><span class="p">,</span> <span class="n">model_request_parameters</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">exc</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fallback_on</span><span class="p">(</span><span class="n">exc</span><span class="p">):</span>
                <span class="n">exceptions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">exc</span><span class="p">)</span>
                <span class="k">continue</span>
            <span class="k">raise</span> <span class="n">exc</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_set_span_attributes</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">response</span><span class="p">,</span> <span class="n">usage</span>

    <span class="k">raise</span> <span class="n">FallbackExceptionGroup</span><span class="p">(</span><span class="s1">'All models from FallbackModel failed'</span><span class="p">,</span> <span class="n">exceptions</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.models.fallback.FallbackModel.request_stream" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">request_stream</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="nf">request_stream</span><span class="p">(</span>
    <span class="n">messages</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">],</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.ModelRequestParameters" href="../base/#pydantic_ai.models.ModelRequestParameters">ModelRequestParameters</a></span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.AsyncIterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator">AsyncIterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.StreamedResponse" href="../base/#pydantic_ai.models.StreamedResponse">StreamedResponse</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Try each model in sequence until one succeeds.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/fallback.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 79</span>
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
<span class="normal">105</span></pre></div></td><td class="code"><div><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code><span class="nd">@asynccontextmanager</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">request_stream</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">StreamedResponse</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Try each model in sequence until one succeeds."""</span>
    <span class="n">exceptions</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">for</span> <span class="n">model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">models</span><span class="p">:</span>
        <span class="k">async</span> <span class="k">with</span> <span class="n">AsyncExitStack</span><span class="p">()</span> <span class="k">as</span> <span class="n">stack</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="n">stack</span><span class="o">.</span><span class="n">enter_async_context</span><span class="p">(</span>
                    <span class="n">model</span><span class="o">.</span><span class="n">request_stream</span><span class="p">(</span><span class="n">messages</span><span class="p">,</span> <span class="n">model_settings</span><span class="p">,</span> <span class="n">model_request_parameters</span><span class="p">)</span>
                <span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">exc</span><span class="p">:</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fallback_on</span><span class="p">(</span><span class="n">exc</span><span class="p">):</span>
                    <span class="n">exceptions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">exc</span><span class="p">)</span>
                    <span class="k">continue</span>
                <span class="k">raise</span> <span class="n">exc</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">_set_span_attributes</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
            <span class="k">yield</span> <span class="n">response</span>
            <span class="k">return</span>

    <span class="k">raise</span> <span class="n">FallbackExceptionGroup</span><span class="p">(</span><span class="s1">'All models from FallbackModel failed'</span><span class="p">,</span> <span class="n">exceptions</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.fallback.FallbackModel.model_name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">model_name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code><span class="n">model_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The model name.</p>
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