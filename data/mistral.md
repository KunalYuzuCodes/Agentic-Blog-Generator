<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/api/models/mistral/">
      
      
        <link rel="prev" href="../instrumented/">
      
      
        <link rel="next" href="../test/">
      
      
      <link rel="icon" href="../../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>pydantic_ai.models.mistral - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="pydantic_ai.models.mistral - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/api/models/mistral.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/api/models/mistral/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="pydantic_ai.models.mistral - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/api/models/mistral.png">
      
    
    
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
      
        
        <a href="#pydantic_aimodelsmistral" class="md-skip">
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
            
              pydantic_ai.models.mistral
            
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
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#setup" class="md-nav__link">
    <span class="md-ellipsis">
      Setup
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Setup">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral" class="md-nav__link">
    <span class="md-ellipsis">
      mistral
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.LatestMistralModelNames" class="md-nav__link">
    <span class="md-ellipsis">
      LatestMistralModelNames
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralModelName" class="md-nav__link">
    <span class="md-ellipsis">
      MistralModelName
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralModelSettings" class="md-nav__link">
    <span class="md-ellipsis">
      MistralModelSettings
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralModel" class="md-nav__link">
    <span class="md-ellipsis">
      MistralModel
    </span>
  </a>
  
    <nav class="md-nav" aria-label="MistralModel">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralModel.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralModel.request" class="md-nav__link">
    <span class="md-ellipsis">
      request
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralModel.request_stream" class="md-nav__link">
    <span class="md-ellipsis">
      request_stream
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralModel.model_name" class="md-nav__link">
    <span class="md-ellipsis">
      model_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralModel.system" class="md-nav__link">
    <span class="md-ellipsis">
      system
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralStreamedResponse" class="md-nav__link">
    <span class="md-ellipsis">
      MistralStreamedResponse
    </span>
  </a>
  
    <nav class="md-nav" aria-label="MistralStreamedResponse">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralStreamedResponse.model_name" class="md-nav__link">
    <span class="md-ellipsis">
      model_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralStreamedResponse.timestamp" class="md-nav__link">
    <span class="md-ellipsis">
      timestamp
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
    </ul>
  
</nav>
      
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
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../fallback/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
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
  <a href="#setup" class="md-nav__link">
    <span class="md-ellipsis">
      Setup
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Setup">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral" class="md-nav__link">
    <span class="md-ellipsis">
      mistral
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.LatestMistralModelNames" class="md-nav__link">
    <span class="md-ellipsis">
      LatestMistralModelNames
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralModelName" class="md-nav__link">
    <span class="md-ellipsis">
      MistralModelName
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralModelSettings" class="md-nav__link">
    <span class="md-ellipsis">
      MistralModelSettings
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralModel" class="md-nav__link">
    <span class="md-ellipsis">
      MistralModel
    </span>
  </a>
  
    <nav class="md-nav" aria-label="MistralModel">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralModel.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralModel.request" class="md-nav__link">
    <span class="md-ellipsis">
      request
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralModel.request_stream" class="md-nav__link">
    <span class="md-ellipsis">
      request_stream
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralModel.model_name" class="md-nav__link">
    <span class="md-ellipsis">
      model_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralModel.system" class="md-nav__link">
    <span class="md-ellipsis">
      system
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralStreamedResponse" class="md-nav__link">
    <span class="md-ellipsis">
      MistralStreamedResponse
    </span>
  </a>
  
    <nav class="md-nav" aria-label="MistralStreamedResponse">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralStreamedResponse.model_name" class="md-nav__link">
    <span class="md-ellipsis">
      model_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.mistral.MistralStreamedResponse.timestamp" class="md-nav__link">
    <span class="md-ellipsis">
      timestamp
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
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
                
                  


  
  


<h1 id="pydantic_aimodelsmistral"><code>pydantic_ai.models.mistral</code></h1>
<h2 id="setup">Setup</h2>
<p>For details on how to set up authentication with this model, see <a href="../../../models/#mistral">model configuration for Mistral</a>.</p>


<div class="doc doc-object doc-module">



<a id="pydantic_ai.models.mistral"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">



















































































































<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.models.mistral.LatestMistralModelNames" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">LatestMistralModelNames</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="n">LatestMistralModelNames</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span>
    <span class="s2">"mistral-large-latest"</span><span class="p">,</span>
    <span class="s2">"mistral-small-latest"</span><span class="p">,</span>
    <span class="s2">"codestral-latest"</span><span class="p">,</span>
    <span class="s2">"mistral-moderation-latest"</span><span class="p">,</span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Latest  Mistral models.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.models.mistral.MistralModelName" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">MistralModelName</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code><span class="n">MistralModelName</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Union" href="https://docs.python.org/3/library/typing.html#typing.Union">Union</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.mistral.LatestMistralModelNames" href="#pydantic_ai.models.mistral.LatestMistralModelNames">LatestMistralModelNames</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Possible Mistral model names.</p>
<p>Since Mistral supports a variety of date-stamped models, we explicitly list the most popular models but
allow any name in the type hints.
Since <a href="https://docs.mistral.ai/getting-started/models/models_overview/">the Mistral docs</a> for a full list.</p>
    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.models.mistral.MistralModelSettings" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">MistralModelSettings</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></code></p>


        <p>Settings used for a Mistral model request.</p>
<p>ALL FIELDS MUST BE <code>mistral_</code> PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/mistral.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span></pre></div></td><td class="code"><div><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="k">class</span><span class="w"> </span><span class="nc">MistralModelSettings</span><span class="p">(</span><span class="n">ModelSettings</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Settings used for a Mistral model request.</span>

<span class="sd">    ALL FIELDS MUST BE `mistral_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.</span>
<span class="sd">    """</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">





  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.models.mistral.MistralModel" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">MistralModel</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../base/#pydantic_ai.models.Model">Model</a></code></p>


        <p>A model that uses Mistral.</p>
<p>Internally, this uses the <a href="https://github.com/mistralai/client-python">Mistral Python client</a> to interact with the API.</p>
<p><a href="https://docs.mistral.ai/">API Documentation</a></p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/mistral.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">102</span>
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
<span class="normal">432</span>
<span class="normal">433</span>
<span class="normal">434</span>
<span class="normal">435</span>
<span class="normal">436</span>
<span class="normal">437</span>
<span class="normal">438</span>
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
<span class="normal">501</span></pre></div></td><td class="code"><div><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code tabindex="0"><span class="nd">@dataclass</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="k">class</span><span class="w"> </span><span class="nc">MistralModel</span><span class="p">(</span><span class="n">Model</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""A model that uses Mistral.</span>

<span class="sd">    Internally, this uses the [Mistral Python client](https://github.com/mistralai/client-python) to interact with the API.</span>

<span class="sd">    [API Documentation](https://docs.mistral.ai/)</span>
<span class="sd">    """</span>

    <span class="n">client</span><span class="p">:</span> <span class="n">Mistral</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">json_mode_schema_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"""Answer in JSON Object, respect the format:</span><span class="se">\n</span><span class="s2">```</span><span class="se">\n</span><span class="si">{schema}</span><span class="se">\n</span><span class="s2">```</span><span class="se">\n</span><span class="s2">"""</span>

    <span class="n">_model_name</span><span class="p">:</span> <span class="n">MistralModelName</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_system</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="s1">'mistral_ai'</span><span class="p">,</span> <span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">model_name</span><span class="p">:</span> <span class="n">MistralModelName</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">provider</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'mistral'</span><span class="p">]</span> <span class="o">|</span> <span class="n">Provider</span><span class="p">[</span><span class="n">Mistral</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'mistral'</span><span class="p">,</span>
        <span class="n">json_mode_schema_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"""Answer in JSON Object, respect the format:</span><span class="se">\n</span><span class="s2">```</span><span class="se">\n</span><span class="si">{schema}</span><span class="se">\n</span><span class="s2">```</span><span class="se">\n</span><span class="s2">"""</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize a Mistral model.</span>

<span class="sd">        Args:</span>
<span class="sd">            model_name: The name of the model to use.</span>
<span class="sd">            provider: The provider to use for authentication and API access. Can be either the string</span>
<span class="sd">                'mistral' or an instance of `Provider[Mistral]`. If not provided, a new provider will be</span>
<span class="sd">                created using the other parameters.</span>
<span class="sd">            json_mode_schema_prompt: The prompt to show when the model expects a JSON object as input.</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_model_name</span> <span class="o">=</span> <span class="n">model_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">json_mode_schema_prompt</span> <span class="o">=</span> <span class="n">json_mode_schema_prompt</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">provider</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">provider</span> <span class="o">=</span> <span class="n">infer_provider</span><span class="p">(</span><span class="n">provider</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">provider</span><span class="o">.</span><span class="n">client</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">base_url</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">sdk_configuration</span><span class="o">.</span><span class="n">get_server_details</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">request</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">tuple</span><span class="p">[</span><span class="n">ModelResponse</span><span class="p">,</span> <span class="n">Usage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Make a non-streaming request to the model from Pydantic AI call."""</span>
        <span class="n">check_allow_model_requests</span><span class="p">()</span>
        <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_completions_create</span><span class="p">(</span>
            <span class="n">messages</span><span class="p">,</span> <span class="n">cast</span><span class="p">(</span><span class="n">MistralModelSettings</span><span class="p">,</span> <span class="n">model_settings</span> <span class="ow">or</span> <span class="p">{}),</span> <span class="n">model_request_parameters</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_process_response</span><span class="p">(</span><span class="n">response</span><span class="p">),</span> <span class="n">_map_usage</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>

    <span class="nd">@asynccontextmanager</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">request_stream</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">StreamedResponse</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Make a streaming request to the model from Pydantic AI call."""</span>
        <span class="n">check_allow_model_requests</span><span class="p">()</span>
        <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_completions_create</span><span class="p">(</span>
            <span class="n">messages</span><span class="p">,</span> <span class="n">cast</span><span class="p">(</span><span class="n">MistralModelSettings</span><span class="p">,</span> <span class="n">model_settings</span> <span class="ow">or</span> <span class="p">{}),</span> <span class="n">model_request_parameters</span>
        <span class="p">)</span>
        <span class="k">async</span> <span class="k">with</span> <span class="n">response</span><span class="p">:</span>
            <span class="k">yield</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_process_streamed_response</span><span class="p">(</span><span class="n">model_request_parameters</span><span class="o">.</span><span class="n">result_tools</span><span class="p">,</span> <span class="n">response</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">model_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">MistralModelName</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""The model name."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model_name</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">system</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""The system / model provider."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_system</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_completions_create</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">MistralModelSettings</span><span class="p">,</span>
        <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">MistralChatCompletionResponse</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Make a non-streaming request to the model."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">chat</span><span class="o">.</span><span class="n">complete_async</span><span class="p">(</span>
                <span class="n">model</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_model_name</span><span class="p">),</span>
                <span class="n">messages</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="n">chain</span><span class="p">(</span><span class="o">*</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_map_message</span><span class="p">(</span><span class="n">m</span><span class="p">)</span> <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="n">messages</span><span class="p">))),</span>
                <span class="n">n</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
                <span class="n">tools</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_map_function_and_result_tools_definition</span><span class="p">(</span><span class="n">model_request_parameters</span><span class="p">)</span> <span class="ow">or</span> <span class="n">UNSET</span><span class="p">,</span>
                <span class="n">tool_choice</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_tool_choice</span><span class="p">(</span><span class="n">model_request_parameters</span><span class="p">),</span>
                <span class="n">stream</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
                <span class="n">max_tokens</span><span class="o">=</span><span class="n">model_settings</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'max_tokens'</span><span class="p">,</span> <span class="n">UNSET</span><span class="p">),</span>
                <span class="n">temperature</span><span class="o">=</span><span class="n">model_settings</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'temperature'</span><span class="p">,</span> <span class="n">UNSET</span><span class="p">),</span>
                <span class="n">top_p</span><span class="o">=</span><span class="n">model_settings</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'top_p'</span><span class="p">,</span> <span class="mi">1</span><span class="p">),</span>
                <span class="n">timeout_ms</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_timeout_ms</span><span class="p">(</span><span class="n">model_settings</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'timeout'</span><span class="p">)),</span>
                <span class="n">random_seed</span><span class="o">=</span><span class="n">model_settings</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'seed'</span><span class="p">,</span> <span class="n">UNSET</span><span class="p">),</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="n">SDKError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">if</span> <span class="p">(</span><span class="n">status_code</span> <span class="o">:=</span> <span class="n">e</span><span class="o">.</span><span class="n">status_code</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mi">400</span><span class="p">:</span>
                <span class="k">raise</span> <span class="n">ModelHTTPError</span><span class="p">(</span><span class="n">status_code</span><span class="o">=</span><span class="n">status_code</span><span class="p">,</span> <span class="n">model_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model_name</span><span class="p">,</span> <span class="n">body</span><span class="o">=</span><span class="n">e</span><span class="o">.</span><span class="n">body</span><span class="p">)</span> <span class="kn">from</span><span class="w"> </span><span class="nn">e</span>
            <span class="k">raise</span>

        <span class="k">assert</span> <span class="n">response</span><span class="p">,</span> <span class="s1">'A unexpected empty response from Mistral.'</span>
        <span class="k">return</span> <span class="n">response</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_stream_completions_create</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">MistralModelSettings</span><span class="p">,</span>
        <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">MistralEventStreamAsync</span><span class="p">[</span><span class="n">MistralCompletionEvent</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Create a streaming completion request to the Mistral model."""</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">MistralEventStreamAsync</span><span class="p">[</span><span class="n">MistralCompletionEvent</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
        <span class="n">mistral_messages</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">chain</span><span class="p">(</span><span class="o">*</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_map_message</span><span class="p">(</span><span class="n">m</span><span class="p">)</span> <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="n">messages</span><span class="p">)))</span>

        <span class="k">if</span> <span class="p">(</span>
            <span class="n">model_request_parameters</span><span class="o">.</span><span class="n">result_tools</span>
            <span class="ow">and</span> <span class="n">model_request_parameters</span><span class="o">.</span><span class="n">function_tools</span>
            <span class="ow">or</span> <span class="n">model_request_parameters</span><span class="o">.</span><span class="n">function_tools</span>
        <span class="p">):</span>
            <span class="c1"># Function Calling</span>
            <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">chat</span><span class="o">.</span><span class="n">stream_async</span><span class="p">(</span>
                <span class="n">model</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_model_name</span><span class="p">),</span>
                <span class="n">messages</span><span class="o">=</span><span class="n">mistral_messages</span><span class="p">,</span>
                <span class="n">n</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
                <span class="n">tools</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_map_function_and_result_tools_definition</span><span class="p">(</span><span class="n">model_request_parameters</span><span class="p">)</span> <span class="ow">or</span> <span class="n">UNSET</span><span class="p">,</span>
                <span class="n">tool_choice</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_tool_choice</span><span class="p">(</span><span class="n">model_request_parameters</span><span class="p">),</span>
                <span class="n">temperature</span><span class="o">=</span><span class="n">model_settings</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'temperature'</span><span class="p">,</span> <span class="n">UNSET</span><span class="p">),</span>
                <span class="n">top_p</span><span class="o">=</span><span class="n">model_settings</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'top_p'</span><span class="p">,</span> <span class="mi">1</span><span class="p">),</span>
                <span class="n">max_tokens</span><span class="o">=</span><span class="n">model_settings</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'max_tokens'</span><span class="p">,</span> <span class="n">UNSET</span><span class="p">),</span>
                <span class="n">timeout_ms</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_get_timeout_ms</span><span class="p">(</span><span class="n">model_settings</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'timeout'</span><span class="p">)),</span>
                <span class="n">presence_penalty</span><span class="o">=</span><span class="n">model_settings</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'presence_penalty'</span><span class="p">),</span>
                <span class="n">frequency_penalty</span><span class="o">=</span><span class="n">model_settings</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'frequency_penalty'</span><span class="p">),</span>
            <span class="p">)</span>

        <span class="k">elif</span> <span class="n">model_request_parameters</span><span class="o">.</span><span class="n">result_tools</span><span class="p">:</span>
            <span class="c1"># Json Mode</span>
            <span class="n">parameters_json_schemas</span> <span class="o">=</span> <span class="p">[</span><span class="n">tool</span><span class="o">.</span><span class="n">parameters_json_schema</span> <span class="k">for</span> <span class="n">tool</span> <span class="ow">in</span> <span class="n">model_request_parameters</span><span class="o">.</span><span class="n">result_tools</span><span class="p">]</span>
            <span class="n">user_output_format_message</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_generate_user_output_format</span><span class="p">(</span><span class="n">parameters_json_schemas</span><span class="p">)</span>
            <span class="n">mistral_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">user_output_format_message</span><span class="p">)</span>

            <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">chat</span><span class="o">.</span><span class="n">stream_async</span><span class="p">(</span>
                <span class="n">model</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_model_name</span><span class="p">),</span>
                <span class="n">messages</span><span class="o">=</span><span class="n">mistral_messages</span><span class="p">,</span>
                <span class="n">response_format</span><span class="o">=</span><span class="p">{</span><span class="s1">'type'</span><span class="p">:</span> <span class="s1">'json_object'</span><span class="p">},</span>
                <span class="n">stream</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># Stream Mode</span>
            <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">chat</span><span class="o">.</span><span class="n">stream_async</span><span class="p">(</span>
                <span class="n">model</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_model_name</span><span class="p">),</span>
                <span class="n">messages</span><span class="o">=</span><span class="n">mistral_messages</span><span class="p">,</span>
                <span class="n">stream</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">assert</span> <span class="n">response</span><span class="p">,</span> <span class="s1">'A unexpected empty response from Mistral.'</span>
        <span class="k">return</span> <span class="n">response</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_get_tool_choice</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">MistralToolChoiceEnum</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get tool choice for the model.</span>

<span class="sd">        - "auto": Default mode. Model decides if it uses the tool or not.</span>
<span class="sd">        - "any": Select any tool.</span>
<span class="sd">        - "none": Prevents tool use.</span>
<span class="sd">        - "required": Forces tool use.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">model_request_parameters</span><span class="o">.</span><span class="n">function_tools</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">model_request_parameters</span><span class="o">.</span><span class="n">result_tools</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>
        <span class="k">elif</span> <span class="ow">not</span> <span class="n">model_request_parameters</span><span class="o">.</span><span class="n">allow_text_result</span><span class="p">:</span>
            <span class="k">return</span> <span class="s1">'required'</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="s1">'auto'</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_map_function_and_result_tools_definition</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">MistralTool</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Map function and result tools to MistralTool format.</span>

<span class="sd">        Returns None if both function_tools and result_tools are empty.</span>
<span class="sd">        """</span>
        <span class="n">all_tools</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ToolDefinition</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">model_request_parameters</span><span class="o">.</span><span class="n">function_tools</span> <span class="o">+</span> <span class="n">model_request_parameters</span><span class="o">.</span><span class="n">result_tools</span>
        <span class="p">)</span>
        <span class="n">tools</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">MistralTool</span><span class="p">(</span>
                <span class="n">function</span><span class="o">=</span><span class="n">MistralFunction</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">r</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">parameters</span><span class="o">=</span><span class="n">r</span><span class="o">.</span><span class="n">parameters_json_schema</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="n">r</span><span class="o">.</span><span class="n">description</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">all_tools</span>
        <span class="p">]</span>
        <span class="k">return</span> <span class="n">tools</span> <span class="k">if</span> <span class="n">tools</span> <span class="k">else</span> <span class="kc">None</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_process_response</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">response</span><span class="p">:</span> <span class="n">MistralChatCompletionResponse</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ModelResponse</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Process a non-streamed response, and prepare a message to return."""</span>
        <span class="k">assert</span> <span class="n">response</span><span class="o">.</span><span class="n">choices</span><span class="p">,</span> <span class="s1">'Unexpected empty response choice.'</span>

        <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">created</span><span class="p">:</span>
            <span class="n">timestamp</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">fromtimestamp</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">created</span><span class="p">,</span> <span class="n">tz</span><span class="o">=</span><span class="n">timezone</span><span class="o">.</span><span class="n">utc</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">timestamp</span> <span class="o">=</span> <span class="n">_now_utc</span><span class="p">()</span>

        <span class="n">choice</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">choices</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
        <span class="n">content</span> <span class="o">=</span> <span class="n">choice</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">content</span>
        <span class="n">tool_calls</span> <span class="o">=</span> <span class="n">choice</span><span class="o">.</span><span class="n">message</span><span class="o">.</span><span class="n">tool_calls</span>

        <span class="n">parts</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelResponsePart</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="n">text</span> <span class="o">:=</span> <span class="n">_map_content</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
            <span class="n">parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">TextPart</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">text</span><span class="p">))</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">tool_calls</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">tool_call</span> <span class="ow">in</span> <span class="n">tool_calls</span><span class="p">:</span>
                <span class="n">tool</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_map_mistral_to_pydantic_tool_call</span><span class="p">(</span><span class="n">tool_call</span><span class="o">=</span><span class="n">tool_call</span><span class="p">)</span>
                <span class="n">parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tool</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">ModelResponse</span><span class="p">(</span><span class="n">parts</span><span class="p">,</span> <span class="n">model_name</span><span class="o">=</span><span class="n">response</span><span class="o">.</span><span class="n">model</span><span class="p">,</span> <span class="n">timestamp</span><span class="o">=</span><span class="n">timestamp</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_process_streamed_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">result_tools</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ToolDefinition</span><span class="p">],</span>
        <span class="n">response</span><span class="p">:</span> <span class="n">MistralEventStreamAsync</span><span class="p">[</span><span class="n">MistralCompletionEvent</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">StreamedResponse</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Process a streamed response, and prepare a streaming response to return."""</span>
        <span class="n">peekable_response</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">PeekableAsyncStream</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>
        <span class="n">first_chunk</span> <span class="o">=</span> <span class="k">await</span> <span class="n">peekable_response</span><span class="o">.</span><span class="n">peek</span><span class="p">()</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">first_chunk</span><span class="p">,</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Unset</span><span class="p">):</span>
            <span class="k">raise</span> <span class="n">UnexpectedModelBehavior</span><span class="p">(</span><span class="s1">'Streamed response ended without content or tool calls'</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">first_chunk</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">created</span><span class="p">:</span>
            <span class="n">timestamp</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">fromtimestamp</span><span class="p">(</span><span class="n">first_chunk</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">created</span><span class="p">,</span> <span class="n">tz</span><span class="o">=</span><span class="n">timezone</span><span class="o">.</span><span class="n">utc</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">timestamp</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">(</span><span class="n">tz</span><span class="o">=</span><span class="n">timezone</span><span class="o">.</span><span class="n">utc</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">MistralStreamedResponse</span><span class="p">(</span>
            <span class="n">_response</span><span class="o">=</span><span class="n">peekable_response</span><span class="p">,</span>
            <span class="n">_model_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_model_name</span><span class="p">,</span>
            <span class="n">_timestamp</span><span class="o">=</span><span class="n">timestamp</span><span class="p">,</span>
            <span class="n">_result_tools</span><span class="o">=</span><span class="p">{</span><span class="n">c</span><span class="o">.</span><span class="n">name</span><span class="p">:</span> <span class="n">c</span> <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">result_tools</span><span class="p">},</span>
        <span class="p">)</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">_map_mistral_to_pydantic_tool_call</span><span class="p">(</span><span class="n">tool_call</span><span class="p">:</span> <span class="n">MistralToolCall</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ToolCallPart</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Maps a MistralToolCall to a ToolCall."""</span>
        <span class="n">tool_call_id</span> <span class="o">=</span> <span class="n">tool_call</span><span class="o">.</span><span class="n">id</span> <span class="ow">or</span> <span class="n">_generate_tool_call_id</span><span class="p">()</span>
        <span class="n">func_call</span> <span class="o">=</span> <span class="n">tool_call</span><span class="o">.</span><span class="n">function</span>

        <span class="k">return</span> <span class="n">ToolCallPart</span><span class="p">(</span><span class="n">func_call</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">func_call</span><span class="o">.</span><span class="n">arguments</span><span class="p">,</span> <span class="n">tool_call_id</span><span class="p">)</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">_map_tool_call</span><span class="p">(</span><span class="n">t</span><span class="p">:</span> <span class="n">ToolCallPart</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">MistralToolCall</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Maps a pydantic-ai ToolCall to a MistralToolCall."""</span>
        <span class="k">return</span> <span class="n">MistralToolCall</span><span class="p">(</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">_utils</span><span class="o">.</span><span class="n">guard_tool_call_id</span><span class="p">(</span><span class="n">t</span><span class="o">=</span><span class="n">t</span><span class="p">),</span>
            <span class="nb">type</span><span class="o">=</span><span class="s1">'function'</span><span class="p">,</span>
            <span class="n">function</span><span class="o">=</span><span class="n">MistralFunctionCall</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="n">t</span><span class="o">.</span><span class="n">tool_name</span><span class="p">,</span> <span class="n">arguments</span><span class="o">=</span><span class="n">t</span><span class="o">.</span><span class="n">args</span><span class="p">),</span>
        <span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_generate_user_output_format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">schemas</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">MistralUserMessage</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get a message with an example of the expected output format."""</span>
        <span class="n">examples</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">schema</span> <span class="ow">in</span> <span class="n">schemas</span><span class="p">:</span>
            <span class="n">typed_dict_definition</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">schema</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'properties'</span><span class="p">,</span> <span class="p">{})</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="n">typed_dict_definition</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_python_type</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
            <span class="n">examples</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">typed_dict_definition</span><span class="p">)</span>

        <span class="n">example_schema</span> <span class="o">=</span> <span class="n">examples</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">examples</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span> <span class="k">else</span> <span class="n">examples</span>
        <span class="k">return</span> <span class="n">MistralUserMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">json_mode_schema_prompt</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">schema</span><span class="o">=</span><span class="n">example_schema</span><span class="p">))</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">_get_python_type</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return a string representation of the Python type for a single JSON schema property.</span>

<span class="sd">        This function handles recursion for nested arrays/objects and `anyOf`.</span>
<span class="sd">        """</span>
        <span class="c1"># 1) Handle anyOf first, because it's a different schema structure</span>
        <span class="k">if</span> <span class="n">any_of</span> <span class="o">:=</span> <span class="n">value</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'anyOf'</span><span class="p">):</span>
            <span class="c1"># Simplistic approach: pick the first option in anyOf</span>
            <span class="c1"># (In reality, you'd possibly want to merge or union types)</span>
            <span class="k">return</span> <span class="sa">f</span><span class="s1">'Optional[</span><span class="si">{</span><span class="bp">cls</span><span class="o">.</span><span class="n">_get_python_type</span><span class="p">(</span><span class="n">any_of</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span><span class="si">}</span><span class="s1">]'</span>

        <span class="c1"># 2) If we have a top-level "type" field</span>
        <span class="n">value_type</span> <span class="o">=</span> <span class="n">value</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'type'</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">value_type</span><span class="p">:</span>
            <span class="c1"># No explicit type; fallback</span>
            <span class="k">return</span> <span class="s1">'Any'</span>

        <span class="c1"># 3) Direct simple type mapping (string, integer, float, bool, None)</span>
        <span class="k">if</span> <span class="n">value_type</span> <span class="ow">in</span> <span class="n">SIMPLE_JSON_TYPE_MAPPING</span> <span class="ow">and</span> <span class="n">value_type</span> <span class="o">!=</span> <span class="s1">'array'</span> <span class="ow">and</span> <span class="n">value_type</span> <span class="o">!=</span> <span class="s1">'object'</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">SIMPLE_JSON_TYPE_MAPPING</span><span class="p">[</span><span class="n">value_type</span><span class="p">]</span>

        <span class="c1"># 4) Array: Recursively get the item type</span>
        <span class="k">if</span> <span class="n">value_type</span> <span class="o">==</span> <span class="s1">'array'</span><span class="p">:</span>
            <span class="n">items</span> <span class="o">=</span> <span class="n">value</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'items'</span><span class="p">,</span> <span class="p">{})</span>
            <span class="k">return</span> <span class="sa">f</span><span class="s1">'list[</span><span class="si">{</span><span class="bp">cls</span><span class="o">.</span><span class="n">_get_python_type</span><span class="p">(</span><span class="n">items</span><span class="p">)</span><span class="si">}</span><span class="s1">]'</span>

        <span class="c1"># 5) Object: Check for additionalProperties</span>
        <span class="k">if</span> <span class="n">value_type</span> <span class="o">==</span> <span class="s1">'object'</span><span class="p">:</span>
            <span class="n">additional_properties</span> <span class="o">=</span> <span class="n">value</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'additionalProperties'</span><span class="p">,</span> <span class="p">{})</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">additional_properties</span><span class="p">,</span> <span class="nb">bool</span><span class="p">):</span>
                <span class="k">return</span> <span class="s1">'bool'</span>  <span class="c1"># pragma: no cover</span>
            <span class="n">additional_properties_type</span> <span class="o">=</span> <span class="n">additional_properties</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'type'</span><span class="p">)</span>
            <span class="k">if</span> <span class="p">(</span>
                <span class="n">additional_properties_type</span> <span class="ow">in</span> <span class="n">SIMPLE_JSON_TYPE_MAPPING</span>
                <span class="ow">and</span> <span class="n">additional_properties_type</span> <span class="o">!=</span> <span class="s1">'array'</span>
                <span class="ow">and</span> <span class="n">additional_properties_type</span> <span class="o">!=</span> <span class="s1">'object'</span>
            <span class="p">):</span>
                <span class="c1"># dict[str, bool/int/float/etc...]</span>
                <span class="k">return</span> <span class="sa">f</span><span class="s1">'dict[str, </span><span class="si">{</span><span class="n">SIMPLE_JSON_TYPE_MAPPING</span><span class="p">[</span><span class="n">additional_properties_type</span><span class="p">]</span><span class="si">}</span><span class="s1">]'</span>
            <span class="k">elif</span> <span class="n">additional_properties_type</span> <span class="o">==</span> <span class="s1">'array'</span><span class="p">:</span>
                <span class="n">array_items</span> <span class="o">=</span> <span class="n">additional_properties</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'items'</span><span class="p">,</span> <span class="p">{})</span>
                <span class="k">return</span> <span class="sa">f</span><span class="s1">'dict[str, list[</span><span class="si">{</span><span class="bp">cls</span><span class="o">.</span><span class="n">_get_python_type</span><span class="p">(</span><span class="n">array_items</span><span class="p">)</span><span class="si">}</span><span class="s1">]]'</span>
            <span class="k">elif</span> <span class="n">additional_properties_type</span> <span class="o">==</span> <span class="s1">'object'</span><span class="p">:</span>
                <span class="c1"># nested dictionary of unknown shape</span>
                <span class="k">return</span> <span class="s1">'dict[str, dict[str, Any]]'</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># If no additionalProperties type or something else, default to a generic dict</span>
                <span class="k">return</span> <span class="s1">'dict[str, Any]'</span>

        <span class="c1"># 6) Fallback</span>
        <span class="k">return</span> <span class="s1">'Any'</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">_get_timeout_ms</span><span class="p">(</span><span class="n">timeout</span><span class="p">:</span> <span class="n">Timeout</span> <span class="o">|</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Convert a timeout to milliseconds."""</span>
        <span class="k">if</span> <span class="n">timeout</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">timeout</span><span class="p">,</span> <span class="nb">float</span><span class="p">):</span>
            <span class="k">return</span> <span class="nb">int</span><span class="p">(</span><span class="mi">1000</span> <span class="o">*</span> <span class="n">timeout</span><span class="p">)</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s1">'Timeout object is not yet supported for MistralModel.'</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">_map_user_message</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">ModelRequest</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterable</span><span class="p">[</span><span class="n">MistralMessages</span><span class="p">]:</span>
        <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">message</span><span class="o">.</span><span class="n">parts</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">SystemPromptPart</span><span class="p">):</span>
                <span class="k">yield</span> <span class="n">MistralSystemMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">part</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">UserPromptPart</span><span class="p">):</span>
                <span class="k">yield</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_map_user_prompt</span><span class="p">(</span><span class="n">part</span><span class="p">)</span>
            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">ToolReturnPart</span><span class="p">):</span>
                <span class="k">yield</span> <span class="n">MistralToolMessage</span><span class="p">(</span>
                    <span class="n">tool_call_id</span><span class="o">=</span><span class="n">part</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">,</span>
                    <span class="n">content</span><span class="o">=</span><span class="n">part</span><span class="o">.</span><span class="n">model_response_str</span><span class="p">(),</span>
                <span class="p">)</span>
            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">RetryPromptPart</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">part</span><span class="o">.</span><span class="n">tool_name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="k">yield</span> <span class="n">MistralUserMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">part</span><span class="o">.</span><span class="n">model_response</span><span class="p">())</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="k">yield</span> <span class="n">MistralToolMessage</span><span class="p">(</span>
                        <span class="n">tool_call_id</span><span class="o">=</span><span class="n">part</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">,</span>
                        <span class="n">content</span><span class="o">=</span><span class="n">part</span><span class="o">.</span><span class="n">model_response</span><span class="p">(),</span>
                    <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">assert_never</span><span class="p">(</span><span class="n">part</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">_map_message</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">ModelMessage</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterable</span><span class="p">[</span><span class="n">MistralMessages</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Just maps a `pydantic_ai.Message` to a `MistralMessage`."""</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">message</span><span class="p">,</span> <span class="n">ModelRequest</span><span class="p">):</span>
            <span class="k">yield from</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_map_user_message</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">message</span><span class="p">,</span> <span class="n">ModelResponse</span><span class="p">):</span>
            <span class="n">content_chunks</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">MistralContentChunk</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">tool_calls</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">MistralToolCall</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

            <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">message</span><span class="o">.</span><span class="n">parts</span><span class="p">:</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">TextPart</span><span class="p">):</span>
                    <span class="n">content_chunks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">MistralTextChunk</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">part</span><span class="o">.</span><span class="n">content</span><span class="p">))</span>
                <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">ToolCallPart</span><span class="p">):</span>
                    <span class="n">tool_calls</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">cls</span><span class="o">.</span><span class="n">_map_tool_call</span><span class="p">(</span><span class="n">part</span><span class="p">))</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">assert_never</span><span class="p">(</span><span class="n">part</span><span class="p">)</span>
            <span class="k">yield</span> <span class="n">MistralAssistantMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">content_chunks</span><span class="p">,</span> <span class="n">tool_calls</span><span class="o">=</span><span class="n">tool_calls</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">assert_never</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">_map_user_prompt</span><span class="p">(</span><span class="n">part</span><span class="p">:</span> <span class="n">UserPromptPart</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">MistralUserMessage</span><span class="p">:</span>
        <span class="n">content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="nb">list</span><span class="p">[</span><span class="n">MistralContentChunk</span><span class="p">]</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">part</span><span class="o">.</span><span class="n">content</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">content</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">part</span><span class="o">.</span><span class="n">content</span><span class="p">:</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
                    <span class="n">content</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">MistralTextChunk</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">item</span><span class="p">))</span>
                <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="n">ImageUrl</span><span class="p">):</span>
                    <span class="n">content</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">MistralImageURLChunk</span><span class="p">(</span><span class="n">image_url</span><span class="o">=</span><span class="n">MistralImageURL</span><span class="p">(</span><span class="n">url</span><span class="o">=</span><span class="n">item</span><span class="o">.</span><span class="n">url</span><span class="p">)))</span>
                <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="n">BinaryContent</span><span class="p">):</span>
                    <span class="n">base64_encoded</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">b64encode</span><span class="p">(</span><span class="n">item</span><span class="o">.</span><span class="n">data</span><span class="p">)</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s1">'utf-8'</span><span class="p">)</span>
                    <span class="k">if</span> <span class="n">item</span><span class="o">.</span><span class="n">is_image</span><span class="p">:</span>
                        <span class="n">image_url</span> <span class="o">=</span> <span class="n">MistralImageURL</span><span class="p">(</span><span class="n">url</span><span class="o">=</span><span class="sa">f</span><span class="s1">'data:</span><span class="si">{</span><span class="n">item</span><span class="o">.</span><span class="n">media_type</span><span class="si">}</span><span class="s1">;base64,</span><span class="si">{</span><span class="n">base64_encoded</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
                        <span class="n">content</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">MistralImageURLChunk</span><span class="p">(</span><span class="n">image_url</span><span class="o">=</span><span class="n">image_url</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s1">'image_url'</span><span class="p">))</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">'Only image binary content is supported for Mistral.'</span><span class="p">)</span>
                <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="n">DocumentUrl</span><span class="p">):</span>
                    <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">'DocumentUrl is not supported in Mistral.'</span><span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
                    <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Unsupported content type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">item</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">MistralUserMessage</span><span class="p">(</span><span class="n">content</span><span class="o">=</span><span class="n">content</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.models.mistral.MistralModel.__init__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__init__</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code tabindex="0"><span class="fm">__init__</span><span class="p">(</span>
    <span class="nf">model_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.mistral.MistralModelName" href="#pydantic_ai.models.mistral.MistralModelName">MistralModelName</a></span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">provider</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s2">"mistral"</span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.providers.Provider" href="../../providers/#pydantic_ai.providers.Provider">Provider</a></span><span class="p">[</span><span class="n"><span title="mistralai.Mistral">Mistral</span></span><span class="p">]</span>
    <span class="p">)</span> <span class="o">=</span> <span class="s2">"mistral"</span><span class="p">,</span>
    <span class="n">json_mode_schema_prompt</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">=</span> <span class="s2">"Answer in JSON Object, respect the format:</span><span class="se">\n</span><span class="s2">```</span><span class="se">\n</span><span class="si">{schema}</span><span class="se">\n</span><span class="s2">```</span><span class="se">\n</span><span class="s2">"</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Initialize a Mistral model.</p>


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
                <code>model_name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.models.mistral.MistralModelName" href="#pydantic_ai.models.mistral.MistralModelName">MistralModelName</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The name of the model to use.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>provider</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a>['mistral'] | <a class="autorefs autorefs-internal" title="pydantic_ai.providers.Provider" href="../../providers/#pydantic_ai.providers.Provider">Provider</a>[<span title="mistralai.Mistral">Mistral</span>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The provider to use for authentication and API access. Can be either the string
'mistral' or an instance of <code>Provider[Mistral]</code>. If not provided, a new provider will be
created using the other parameters.</p>
              </div>
            </td>
            <td>
                  <code>'mistral'</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>json_mode_schema_prompt</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The prompt to show when the model expects a JSON object as input.</p>
              </div>
            </td>
            <td>
                  <code>'Answer in JSON Object, respect the format:\n```\n{schema}\n```\n'</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/mistral.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">117</span>
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
<span class="normal">138</span></pre></div></td><td class="code"><div><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">model_name</span><span class="p">:</span> <span class="n">MistralModelName</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">provider</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'mistral'</span><span class="p">]</span> <span class="o">|</span> <span class="n">Provider</span><span class="p">[</span><span class="n">Mistral</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'mistral'</span><span class="p">,</span>
    <span class="n">json_mode_schema_prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"""Answer in JSON Object, respect the format:</span><span class="se">\n</span><span class="s2">```</span><span class="se">\n</span><span class="si">{schema}</span><span class="se">\n</span><span class="s2">```</span><span class="se">\n</span><span class="s2">"""</span><span class="p">,</span>
<span class="p">):</span>
<span class="w">    </span><span class="sd">"""Initialize a Mistral model.</span>

<span class="sd">    Args:</span>
<span class="sd">        model_name: The name of the model to use.</span>
<span class="sd">        provider: The provider to use for authentication and API access. Can be either the string</span>
<span class="sd">            'mistral' or an instance of `Provider[Mistral]`. If not provided, a new provider will be</span>
<span class="sd">            created using the other parameters.</span>
<span class="sd">        json_mode_schema_prompt: The prompt to show when the model expects a JSON object as input.</span>
<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_model_name</span> <span class="o">=</span> <span class="n">model_name</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">json_mode_schema_prompt</span> <span class="o">=</span> <span class="n">json_mode_schema_prompt</span>

    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">provider</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">provider</span> <span class="o">=</span> <span class="n">infer_provider</span><span class="p">(</span><span class="n">provider</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">provider</span><span class="o">.</span><span class="n">client</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.models.mistral.MistralModel.request" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">request</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code><span class="nf">request</span><span class="p">(</span>
    <span class="n">messages</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">],</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.ModelRequestParameters" href="../base/#pydantic_ai.models.ModelRequestParameters">ModelRequestParameters</a></span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple">tuple</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponse" href="../../messages/#pydantic_ai.messages.ModelResponse">ModelResponse</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.Usage" href="../../usage/#pydantic_ai.usage.Usage">Usage</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Make a non-streaming request to the model from Pydantic AI call.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/mistral.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">144</span>
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
<span class="normal">155</span></pre></div></td><td class="code"><div><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">request</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">tuple</span><span class="p">[</span><span class="n">ModelResponse</span><span class="p">,</span> <span class="n">Usage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Make a non-streaming request to the model from Pydantic AI call."""</span>
    <span class="n">check_allow_model_requests</span><span class="p">()</span>
    <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_completions_create</span><span class="p">(</span>
        <span class="n">messages</span><span class="p">,</span> <span class="n">cast</span><span class="p">(</span><span class="n">MistralModelSettings</span><span class="p">,</span> <span class="n">model_settings</span> <span class="ow">or</span> <span class="p">{}),</span> <span class="n">model_request_parameters</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_process_response</span><span class="p">(</span><span class="n">response</span><span class="p">),</span> <span class="n">_map_usage</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.models.mistral.MistralModel.request_stream" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">request_stream</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code><span class="nf">request_stream</span><span class="p">(</span>
    <span class="n">messages</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">],</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.ModelRequestParameters" href="../base/#pydantic_ai.models.ModelRequestParameters">ModelRequestParameters</a></span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.AsyncIterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator">AsyncIterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.StreamedResponse" href="../base/#pydantic_ai.models.StreamedResponse">StreamedResponse</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Make a streaming request to the model from Pydantic AI call.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/mistral.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">157</span>
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
<span class="normal">170</span></pre></div></td><td class="code"><div><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code><span class="nd">@asynccontextmanager</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">request_stream</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">StreamedResponse</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Make a streaming request to the model from Pydantic AI call."""</span>
    <span class="n">check_allow_model_requests</span><span class="p">()</span>
    <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_completions_create</span><span class="p">(</span>
        <span class="n">messages</span><span class="p">,</span> <span class="n">cast</span><span class="p">(</span><span class="n">MistralModelSettings</span><span class="p">,</span> <span class="n">model_settings</span> <span class="ow">or</span> <span class="p">{}),</span> <span class="n">model_request_parameters</span>
    <span class="p">)</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">response</span><span class="p">:</span>
        <span class="k">yield</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_process_streamed_response</span><span class="p">(</span><span class="n">model_request_parameters</span><span class="o">.</span><span class="n">result_tools</span><span class="p">,</span> <span class="n">response</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.mistral.MistralModel.model_name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">model_name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code><span class="n">model_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.mistral.MistralModelName" href="#pydantic_ai.models.mistral.MistralModelName">MistralModelName</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The model name.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.mistral.MistralModel.system" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">system</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_11"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_11 > code"></button><code><span class="n">system</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The system / model provider.</p>
    </div>

</div>




















































  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.models.mistral.MistralStreamedResponse" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">MistralStreamedResponse</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_ai.models.StreamedResponse" href="../base/#pydantic_ai.models.StreamedResponse">StreamedResponse</a></code></p>


        <p>Implementation of <code>StreamedResponse</code> for Mistral models.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/mistral.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">507</span>
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
<span class="normal">546</span>
<span class="normal">547</span>
<span class="normal">548</span>
<span class="normal">549</span>
<span class="normal">550</span>
<span class="normal">551</span>
<span class="normal">552</span>
<span class="normal">553</span>
<span class="normal">554</span>
<span class="normal">555</span>
<span class="normal">556</span>
<span class="normal">557</span>
<span class="normal">558</span>
<span class="normal">559</span>
<span class="normal">560</span>
<span class="normal">561</span>
<span class="normal">562</span>
<span class="normal">563</span>
<span class="normal">564</span>
<span class="normal">565</span>
<span class="normal">566</span>
<span class="normal">567</span>
<span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span>
<span class="normal">571</span>
<span class="normal">572</span>
<span class="normal">573</span>
<span class="normal">574</span>
<span class="normal">575</span>
<span class="normal">576</span>
<span class="normal">577</span>
<span class="normal">578</span>
<span class="normal">579</span>
<span class="normal">580</span>
<span class="normal">581</span>
<span class="normal">582</span>
<span class="normal">583</span>
<span class="normal">584</span>
<span class="normal">585</span>
<span class="normal">586</span>
<span class="normal">587</span>
<span class="normal">588</span>
<span class="normal">589</span>
<span class="normal">590</span>
<span class="normal">591</span>
<span class="normal">592</span>
<span class="normal">593</span>
<span class="normal">594</span>
<span class="normal">595</span>
<span class="normal">596</span>
<span class="normal">597</span>
<span class="normal">598</span>
<span class="normal">599</span>
<span class="normal">600</span>
<span class="normal">601</span>
<span class="normal">602</span>
<span class="normal">603</span>
<span class="normal">604</span>
<span class="normal">605</span>
<span class="normal">606</span>
<span class="normal">607</span></pre></div></td><td class="code"><div><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">MistralStreamedResponse</span><span class="p">(</span><span class="n">StreamedResponse</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Implementation of `StreamedResponse` for Mistral models."""</span>

    <span class="n">_model_name</span><span class="p">:</span> <span class="n">MistralModelName</span>
    <span class="n">_response</span><span class="p">:</span> <span class="n">AsyncIterable</span><span class="p">[</span><span class="n">MistralCompletionEvent</span><span class="p">]</span>
    <span class="n">_timestamp</span><span class="p">:</span> <span class="n">datetime</span>
    <span class="n">_result_tools</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">ToolDefinition</span><span class="p">]</span>

    <span class="n">_delta_content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="s1">''</span><span class="p">,</span> <span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_get_event_iterator</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">ModelResponseStreamEvent</span><span class="p">]:</span>
        <span class="n">chunk</span><span class="p">:</span> <span class="n">MistralCompletionEvent</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_response</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_usage</span> <span class="o">+=</span> <span class="n">_map_usage</span><span class="p">(</span><span class="n">chunk</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>

            <span class="k">try</span><span class="p">:</span>
                <span class="n">choice</span> <span class="o">=</span> <span class="n">chunk</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">choices</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
            <span class="k">except</span> <span class="ne">IndexError</span><span class="p">:</span>
                <span class="k">continue</span>

            <span class="c1"># Handle the text part of the response</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">choice</span><span class="o">.</span><span class="n">delta</span><span class="o">.</span><span class="n">content</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">_map_content</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">text</span><span class="p">:</span>
                <span class="c1"># Attempt to produce a result tool call from the received text</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_tools</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_delta_content</span> <span class="o">+=</span> <span class="n">text</span>
                    <span class="n">maybe_tool_call_part</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_try_get_result_tool_from_text</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_delta_content</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_tools</span><span class="p">)</span>
                    <span class="k">if</span> <span class="n">maybe_tool_call_part</span><span class="p">:</span>
                        <span class="k">yield</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parts_manager</span><span class="o">.</span><span class="n">handle_tool_call_part</span><span class="p">(</span>
                            <span class="n">vendor_part_id</span><span class="o">=</span><span class="s1">'result'</span><span class="p">,</span>
                            <span class="n">tool_name</span><span class="o">=</span><span class="n">maybe_tool_call_part</span><span class="o">.</span><span class="n">tool_name</span><span class="p">,</span>
                            <span class="n">args</span><span class="o">=</span><span class="n">maybe_tool_call_part</span><span class="o">.</span><span class="n">args_as_dict</span><span class="p">(),</span>
                            <span class="n">tool_call_id</span><span class="o">=</span><span class="n">maybe_tool_call_part</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">,</span>
                        <span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="k">yield</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parts_manager</span><span class="o">.</span><span class="n">handle_text_delta</span><span class="p">(</span><span class="n">vendor_part_id</span><span class="o">=</span><span class="s1">'content'</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">text</span><span class="p">)</span>

            <span class="c1"># Handle the explicit tool calls</span>
            <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">dtc</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">choice</span><span class="o">.</span><span class="n">delta</span><span class="o">.</span><span class="n">tool_calls</span> <span class="ow">or</span> <span class="p">[]):</span>
                <span class="c1"># It seems that mistral just sends full tool calls, so we just use them directly, rather than building</span>
                <span class="k">yield</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parts_manager</span><span class="o">.</span><span class="n">handle_tool_call_part</span><span class="p">(</span>
                    <span class="n">vendor_part_id</span><span class="o">=</span><span class="n">index</span><span class="p">,</span> <span class="n">tool_name</span><span class="o">=</span><span class="n">dtc</span><span class="o">.</span><span class="n">function</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="n">dtc</span><span class="o">.</span><span class="n">function</span><span class="o">.</span><span class="n">arguments</span><span class="p">,</span> <span class="n">tool_call_id</span><span class="o">=</span><span class="n">dtc</span><span class="o">.</span><span class="n">id</span>
                <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">model_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">MistralModelName</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the model name of the response."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model_name</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">timestamp</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">datetime</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the timestamp of the response."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_timestamp</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">_try_get_result_tool_from_text</span><span class="p">(</span><span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">result_tools</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">ToolDefinition</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ToolCallPart</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">output_json</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="n">pydantic_core</span><span class="o">.</span><span class="n">from_json</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">allow_partial</span><span class="o">=</span><span class="s1">'trailing-strings'</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">output_json</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">result_tool</span> <span class="ow">in</span> <span class="n">result_tools</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
                <span class="c1"># NOTE: Additional verification to prevent JSON validation to crash in `_result.py`</span>
                <span class="c1"># Ensures required parameters in the JSON schema are respected, especially for stream-based return types.</span>
                <span class="c1"># Example with BaseModel and required fields.</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="n">MistralStreamedResponse</span><span class="o">.</span><span class="n">_validate_required_json_schema</span><span class="p">(</span>
                    <span class="n">output_json</span><span class="p">,</span> <span class="n">result_tool</span><span class="o">.</span><span class="n">parameters_json_schema</span>
                <span class="p">):</span>
                    <span class="k">continue</span>

                <span class="c1"># The following part_id will be thrown away</span>
                <span class="k">return</span> <span class="n">ToolCallPart</span><span class="p">(</span><span class="n">tool_name</span><span class="o">=</span><span class="n">result_tool</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="n">output_json</span><span class="p">)</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">_validate_required_json_schema</span><span class="p">(</span><span class="n">json_dict</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">json_schema</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Validate that all required parameters in the JSON schema are present in the JSON dictionary."""</span>
        <span class="n">required_params</span> <span class="o">=</span> <span class="n">json_schema</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'required'</span><span class="p">,</span> <span class="p">[])</span>
        <span class="n">properties</span> <span class="o">=</span> <span class="n">json_schema</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'properties'</span><span class="p">,</span> <span class="p">{})</span>

        <span class="k">for</span> <span class="n">param</span> <span class="ow">in</span> <span class="n">required_params</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">param</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">json_dict</span><span class="p">:</span>
                <span class="k">return</span> <span class="kc">False</span>

            <span class="n">param_schema</span> <span class="o">=</span> <span class="n">properties</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">param</span><span class="p">,</span> <span class="p">{})</span>
            <span class="n">param_type</span> <span class="o">=</span> <span class="n">param_schema</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'type'</span><span class="p">)</span>
            <span class="n">param_items_type</span> <span class="o">=</span> <span class="n">param_schema</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'items'</span><span class="p">,</span> <span class="p">{})</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'type'</span><span class="p">)</span>

            <span class="k">if</span> <span class="n">param_type</span> <span class="o">==</span> <span class="s1">'array'</span> <span class="ow">and</span> <span class="n">param_items_type</span><span class="p">:</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">json_dict</span><span class="p">[</span><span class="n">param</span><span class="p">],</span> <span class="nb">list</span><span class="p">):</span>
                    <span class="k">return</span> <span class="kc">False</span>
                <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">json_dict</span><span class="p">[</span><span class="n">param</span><span class="p">]:</span>
                    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="n">VALID_JSON_TYPE_MAPPING</span><span class="p">[</span><span class="n">param_items_type</span><span class="p">]):</span>
                        <span class="k">return</span> <span class="kc">False</span>
            <span class="k">elif</span> <span class="n">param_type</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">json_dict</span><span class="p">[</span><span class="n">param</span><span class="p">],</span> <span class="n">VALID_JSON_TYPE_MAPPING</span><span class="p">[</span><span class="n">param_type</span><span class="p">]):</span>
                <span class="k">return</span> <span class="kc">False</span>

            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">json_dict</span><span class="p">[</span><span class="n">param</span><span class="p">],</span> <span class="nb">dict</span><span class="p">)</span> <span class="ow">and</span> <span class="s1">'properties'</span> <span class="ow">in</span> <span class="n">param_schema</span><span class="p">:</span>
                <span class="n">nested_schema</span> <span class="o">=</span> <span class="n">param_schema</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="n">MistralStreamedResponse</span><span class="o">.</span><span class="n">_validate_required_json_schema</span><span class="p">(</span><span class="n">json_dict</span><span class="p">[</span><span class="n">param</span><span class="p">],</span> <span class="n">nested_schema</span><span class="p">):</span>
                    <span class="k">return</span> <span class="kc">False</span>

        <span class="k">return</span> <span class="kc">True</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.mistral.MistralStreamedResponse.model_name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">model_name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_13"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_13 > code"></button><code><span class="n">model_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.mistral.MistralModelName" href="#pydantic_ai.models.mistral.MistralModelName">MistralModelName</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Get the model name of the response.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.mistral.MistralStreamedResponse.timestamp" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">timestamp</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_14"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_14 > code"></button><code><span class="n">timestamp</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="datetime.datetime" href="https://docs.python.org/3/library/datetime.html#datetime.datetime">datetime</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Get the timestamp of the response.</p>
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