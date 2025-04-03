<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/api/models/function/">
      
      
        <link rel="prev" href="../test/">
      
      
        <link rel="next" href="../fallback/">
      
      
      <link rel="icon" href="../../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>pydantic_ai.models.function - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="pydantic_ai.models.function - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/api/models/function.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/api/models/function/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="pydantic_ai.models.function - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/api/models/function.png">
      
    
    
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
      
        
        <a href="#pydantic_aimodelsfunction" class="md-skip">
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
            
              pydantic_ai.models.function
            
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
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.function" class="md-nav__link">
    <span class="md-ellipsis">
      function
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.FunctionModel" class="md-nav__link">
    <span class="md-ellipsis">
      FunctionModel
    </span>
  </a>
  
    <nav class="md-nav" aria-label="FunctionModel">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.FunctionModel.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.FunctionModel.model_name" class="md-nav__link">
    <span class="md-ellipsis">
      model_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.FunctionModel.system" class="md-nav__link">
    <span class="md-ellipsis">
      system
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.AgentInfo" class="md-nav__link">
    <span class="md-ellipsis">
      AgentInfo
    </span>
  </a>
  
    <nav class="md-nav" aria-label="AgentInfo">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.AgentInfo.function_tools" class="md-nav__link">
    <span class="md-ellipsis">
      function_tools
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.AgentInfo.allow_text_result" class="md-nav__link">
    <span class="md-ellipsis">
      allow_text_result
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.AgentInfo.result_tools" class="md-nav__link">
    <span class="md-ellipsis">
      result_tools
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.AgentInfo.model_settings" class="md-nav__link">
    <span class="md-ellipsis">
      model_settings
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.DeltaToolCall" class="md-nav__link">
    <span class="md-ellipsis">
      DeltaToolCall
    </span>
  </a>
  
    <nav class="md-nav" aria-label="DeltaToolCall">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.DeltaToolCall.name" class="md-nav__link">
    <span class="md-ellipsis">
      name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.DeltaToolCall.json_args" class="md-nav__link">
    <span class="md-ellipsis">
      json_args
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.DeltaToolCall.tool_call_id" class="md-nav__link">
    <span class="md-ellipsis">
      tool_call_id
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.DeltaToolCalls" class="md-nav__link">
    <span class="md-ellipsis">
      DeltaToolCalls
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.FunctionDef" class="md-nav__link">
    <span class="md-ellipsis">
      FunctionDef
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.StreamFunctionDef" class="md-nav__link">
    <span class="md-ellipsis">
      StreamFunctionDef
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.FunctionStreamedResponse" class="md-nav__link">
    <span class="md-ellipsis">
      FunctionStreamedResponse
    </span>
  </a>
  
    <nav class="md-nav" aria-label="FunctionStreamedResponse">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.FunctionStreamedResponse.model_name" class="md-nav__link">
    <span class="md-ellipsis">
      model_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.FunctionStreamedResponse.timestamp" class="md-nav__link">
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
  <a href="#pydantic_ai.models.function" class="md-nav__link">
    <span class="md-ellipsis">
      function
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.FunctionModel" class="md-nav__link">
    <span class="md-ellipsis">
      FunctionModel
    </span>
  </a>
  
    <nav class="md-nav" aria-label="FunctionModel">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.FunctionModel.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.FunctionModel.model_name" class="md-nav__link">
    <span class="md-ellipsis">
      model_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.FunctionModel.system" class="md-nav__link">
    <span class="md-ellipsis">
      system
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.AgentInfo" class="md-nav__link">
    <span class="md-ellipsis">
      AgentInfo
    </span>
  </a>
  
    <nav class="md-nav" aria-label="AgentInfo">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.AgentInfo.function_tools" class="md-nav__link">
    <span class="md-ellipsis">
      function_tools
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.AgentInfo.allow_text_result" class="md-nav__link">
    <span class="md-ellipsis">
      allow_text_result
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.AgentInfo.result_tools" class="md-nav__link">
    <span class="md-ellipsis">
      result_tools
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.AgentInfo.model_settings" class="md-nav__link">
    <span class="md-ellipsis">
      model_settings
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.DeltaToolCall" class="md-nav__link">
    <span class="md-ellipsis">
      DeltaToolCall
    </span>
  </a>
  
    <nav class="md-nav" aria-label="DeltaToolCall">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.DeltaToolCall.name" class="md-nav__link">
    <span class="md-ellipsis">
      name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.DeltaToolCall.json_args" class="md-nav__link">
    <span class="md-ellipsis">
      json_args
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.DeltaToolCall.tool_call_id" class="md-nav__link">
    <span class="md-ellipsis">
      tool_call_id
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.DeltaToolCalls" class="md-nav__link">
    <span class="md-ellipsis">
      DeltaToolCalls
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.FunctionDef" class="md-nav__link">
    <span class="md-ellipsis">
      FunctionDef
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.StreamFunctionDef" class="md-nav__link">
    <span class="md-ellipsis">
      StreamFunctionDef
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.FunctionStreamedResponse" class="md-nav__link">
    <span class="md-ellipsis">
      FunctionStreamedResponse
    </span>
  </a>
  
    <nav class="md-nav" aria-label="FunctionStreamedResponse">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.FunctionStreamedResponse.model_name" class="md-nav__link">
    <span class="md-ellipsis">
      model_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.function.FunctionStreamedResponse.timestamp" class="md-nav__link">
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
                  </div>
                </div>
              </div>
            
          
          
            <div class="md-content" data-md-component="content">
              <article class="md-content__inner md-typeset">
                
                  


  
  


<h1 id="pydantic_aimodelsfunction"><code>pydantic_ai.models.function</code></h1>
<p>A model controlled by a local function.</p>
<p><a class="autorefs autorefs-internal" href="#pydantic_ai.models.function.FunctionModel"><code>FunctionModel</code></a> is similar to <a href="../test/"><code>TestModel</code></a>,
but allows greater control over the model's behavior.</p>
<p>Its primary use case is for more advanced unit testing than is possible with <code>TestModel</code>.</p>
<p>Here's a minimal example:</p>
<div class="language-py highlight"><span class="filename">function_model_usage.py</span><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.messages</span><span class="w"> </span><span class="kn">import</span> <span class="n">ModelMessage</span><span class="p">,</span> <span class="n">ModelResponse</span><span class="p">,</span> <span class="n">TextPart</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.function</span><span class="w"> </span><span class="kn">import</span> <span class="n">FunctionModel</span><span class="p">,</span> <span class="n">AgentInfo</span>

<span class="n">my_agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'openai:gpt-4o'</span><span class="p">)</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">model_function</span><span class="p">(</span>
    <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span> <span class="n">info</span><span class="p">:</span> <span class="n">AgentInfo</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ModelResponse</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    [</span>
<span class="sd">        ModelRequest(</span>
<span class="sd">            parts=[</span>
<span class="sd">                UserPromptPart(</span>
<span class="sd">                    content='Testing my agent...',</span>
<span class="sd">                    timestamp=datetime.datetime(...),</span>
<span class="sd">                    part_kind='user-prompt',</span>
<span class="sd">                )</span>
<span class="sd">            ],</span>
<span class="sd">            kind='request',</span>
<span class="sd">        )</span>
<span class="sd">    ]</span>
<span class="sd">    """</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">info</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    AgentInfo(</span>
<span class="sd">        function_tools=[], allow_text_result=True, result_tools=[], model_settings=None</span>
<span class="sd">    )</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">ModelResponse</span><span class="p">(</span><span class="n">parts</span><span class="o">=</span><span class="p">[</span><span class="n">TextPart</span><span class="p">(</span><span class="s1">'hello world'</span><span class="p">)])</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">test_my_agent</span><span class="p">():</span>
<span class="w">    </span><span class="sd">"""Unit test for my_agent, to be run by pytest."""</span>
    <span class="k">with</span> <span class="n">my_agent</span><span class="o">.</span><span class="n">override</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="n">FunctionModel</span><span class="p">(</span><span class="n">model_function</span><span class="p">)):</span>
        <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">my_agent</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="s1">'Testing my agent...'</span><span class="p">)</span>
        <span class="k">assert</span> <span class="n">result</span><span class="o">.</span><span class="n">data</span> <span class="o">==</span> <span class="s1">'hello world'</span>
</code></pre></div>
<p>See <a href="../../../testing/#unit-testing-with-functionmodel">Unit testing with <code>FunctionModel</code></a> for detailed documentation.</p>


<div class="doc doc-object doc-module">



<a id="pydantic_ai.models.function"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">



























































































<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.models.function.FunctionModel" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">FunctionModel</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../base/#pydantic_ai.models.Model">Model</a></code></p>


        <p>A model controlled by a local function.</p>
<p>Apart from <code>__init__</code>, all methods are private or match those of the base class.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/function.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 37</span>
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
<span class="normal">145</span></pre></div></td><td class="code"><div><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code tabindex="0"><span class="nd">@dataclass</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="k">class</span><span class="w"> </span><span class="nc">FunctionModel</span><span class="p">(</span><span class="n">Model</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""A model controlled by a local function.</span>

<span class="sd">    Apart from `__init__`, all methods are private or match those of the base class.</span>
<span class="sd">    """</span>

    <span class="n">function</span><span class="p">:</span> <span class="n">FunctionDef</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">stream_function</span><span class="p">:</span> <span class="n">StreamFunctionDef</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="n">_model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_system</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="s1">'function'</span><span class="p">,</span> <span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">function</span><span class="p">:</span> <span class="n">FunctionDef</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">stream_function</span><span class="p">:</span> <span class="n">StreamFunctionDef</span><span class="p">,</span> <span class="n">model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">function</span><span class="p">:</span> <span class="n">FunctionDef</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">stream_function</span><span class="p">:</span> <span class="n">StreamFunctionDef</span><span class="p">,</span> <span class="n">model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span> <span class="o">...</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">function</span><span class="p">:</span> <span class="n">FunctionDef</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">stream_function</span><span class="p">:</span> <span class="n">StreamFunctionDef</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Initialize a `FunctionModel`.</span>

<span class="sd">        Either `function` or `stream_function` must be provided, providing both is allowed.</span>

<span class="sd">        Args:</span>
<span class="sd">            function: The function to call for non-streamed requests.</span>
<span class="sd">            stream_function: The function to call for streamed requests.</span>
<span class="sd">            model_name: The name of the model. If not provided, a name is generated from the function names.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">function</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">stream_function</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s1">'Either `function` or `stream_function` must be provided'</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">function</span> <span class="o">=</span> <span class="n">function</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">stream_function</span> <span class="o">=</span> <span class="n">stream_function</span>

        <span class="n">function_name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">function</span><span class="o">.</span><span class="vm">__name__</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">function</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="s1">''</span>
        <span class="n">stream_function_name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">stream_function</span><span class="o">.</span><span class="vm">__name__</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">stream_function</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="s1">''</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_model_name</span> <span class="o">=</span> <span class="n">model_name</span> <span class="ow">or</span> <span class="sa">f</span><span class="s1">'function:</span><span class="si">{</span><span class="n">function_name</span><span class="si">}</span><span class="s1">:</span><span class="si">{</span><span class="n">stream_function_name</span><span class="si">}</span><span class="s1">'</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">request</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">tuple</span><span class="p">[</span><span class="n">ModelResponse</span><span class="p">,</span> <span class="n">usage</span><span class="o">.</span><span class="n">Usage</span><span class="p">]:</span>
        <span class="n">agent_info</span> <span class="o">=</span> <span class="n">AgentInfo</span><span class="p">(</span>
            <span class="n">model_request_parameters</span><span class="o">.</span><span class="n">function_tools</span><span class="p">,</span>
            <span class="n">model_request_parameters</span><span class="o">.</span><span class="n">allow_text_result</span><span class="p">,</span>
            <span class="n">model_request_parameters</span><span class="o">.</span><span class="n">result_tools</span><span class="p">,</span>
            <span class="n">model_settings</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">function</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'FunctionModel must receive a `function` to support non-streamed requests'</span>

        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">iscoroutinefunction</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">function</span><span class="p">):</span>
            <span class="n">response</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">function</span><span class="p">(</span><span class="n">messages</span><span class="p">,</span> <span class="n">agent_info</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">response_</span> <span class="o">=</span> <span class="k">await</span> <span class="n">_utils</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">function</span><span class="p">,</span> <span class="n">messages</span><span class="p">,</span> <span class="n">agent_info</span><span class="p">)</span>
            <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response_</span><span class="p">,</span> <span class="n">ModelResponse</span><span class="p">),</span> <span class="n">response_</span>
            <span class="n">response</span> <span class="o">=</span> <span class="n">response_</span>
        <span class="n">response</span><span class="o">.</span><span class="n">model_name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model_name</span>
        <span class="c1"># TODO is `messages` right here? Should it just be new messages?</span>
        <span class="k">return</span> <span class="n">response</span><span class="p">,</span> <span class="n">_estimate_usage</span><span class="p">(</span><span class="n">chain</span><span class="p">(</span><span class="n">messages</span><span class="p">,</span> <span class="p">[</span><span class="n">response</span><span class="p">]))</span>

    <span class="nd">@asynccontextmanager</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">request_stream</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">StreamedResponse</span><span class="p">]:</span>
        <span class="n">agent_info</span> <span class="o">=</span> <span class="n">AgentInfo</span><span class="p">(</span>
            <span class="n">model_request_parameters</span><span class="o">.</span><span class="n">function_tools</span><span class="p">,</span>
            <span class="n">model_request_parameters</span><span class="o">.</span><span class="n">allow_text_result</span><span class="p">,</span>
            <span class="n">model_request_parameters</span><span class="o">.</span><span class="n">result_tools</span><span class="p">,</span>
            <span class="n">model_settings</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">stream_function</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="p">(</span>
            <span class="s1">'FunctionModel must receive a `stream_function` to support streamed requests'</span>
        <span class="p">)</span>

        <span class="n">response_stream</span> <span class="o">=</span> <span class="n">PeekableAsyncStream</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">stream_function</span><span class="p">(</span><span class="n">messages</span><span class="p">,</span> <span class="n">agent_info</span><span class="p">))</span>

        <span class="n">first</span> <span class="o">=</span> <span class="k">await</span> <span class="n">response_stream</span><span class="o">.</span><span class="n">peek</span><span class="p">()</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">first</span><span class="p">,</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Unset</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">'Stream function must return at least one item'</span><span class="p">)</span>

        <span class="k">yield</span> <span class="n">FunctionStreamedResponse</span><span class="p">(</span><span class="n">_model_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_model_name</span><span class="p">,</span> <span class="n">_iter</span><span class="o">=</span><span class="n">response_stream</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">model_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""The model name."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model_name</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">system</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""The system / model provider."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_system</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.models.function.FunctionModel.__init__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__init__</span>


</h4>
          <div class="doc-overloads">
<div class="language-python doc-signature highlight"><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="nf">function</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.function.FunctionDef" href="#pydantic_ai.models.function.FunctionDef">FunctionDef</a></span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">model_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">stream_function</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.function.StreamFunctionDef" href="#pydantic_ai.models.function.StreamFunctionDef">StreamFunctionDef</a></span><span class="p">,</span>
    <span class="n">model_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="nf">function</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.function.FunctionDef" href="#pydantic_ai.models.function.FunctionDef">FunctionDef</a></span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">stream_function</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.function.StreamFunctionDef" href="#pydantic_ai.models.function.StreamFunctionDef">StreamFunctionDef</a></span><span class="p">,</span>
    <span class="n">model_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>          </div>
<div class="language-python doc-signature highlight"><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="nf">function</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.function.FunctionDef" href="#pydantic_ai.models.function.FunctionDef">FunctionDef</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">stream_function</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.function.StreamFunctionDef" href="#pydantic_ai.models.function.StreamFunctionDef">StreamFunctionDef</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Initialize a <code>FunctionModel</code>.</p>
<p>Either <code>function</code> or <code>stream_function</code> must be provided, providing both is allowed.</p>


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
                <code>function</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.models.function.FunctionDef" href="#pydantic_ai.models.function.FunctionDef">FunctionDef</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The function to call for non-streamed requests.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>stream_function</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.models.function.StreamFunctionDef" href="#pydantic_ai.models.function.StreamFunctionDef">StreamFunctionDef</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The function to call for streamed requests.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>model_name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The name of the model. If not provided, a name is generated from the function names.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/function.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">61</span>
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
<span class="normal">84</span></pre></div></td><td class="code"><div><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">function</span><span class="p">:</span> <span class="n">FunctionDef</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">stream_function</span><span class="p">:</span> <span class="n">StreamFunctionDef</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">):</span>
<span class="w">    </span><span class="sd">"""Initialize a `FunctionModel`.</span>

<span class="sd">    Either `function` or `stream_function` must be provided, providing both is allowed.</span>

<span class="sd">    Args:</span>
<span class="sd">        function: The function to call for non-streamed requests.</span>
<span class="sd">        stream_function: The function to call for streamed requests.</span>
<span class="sd">        model_name: The name of the model. If not provided, a name is generated from the function names.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">function</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">stream_function</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s1">'Either `function` or `stream_function` must be provided'</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">function</span> <span class="o">=</span> <span class="n">function</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">stream_function</span> <span class="o">=</span> <span class="n">stream_function</span>

    <span class="n">function_name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">function</span><span class="o">.</span><span class="vm">__name__</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">function</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="s1">''</span>
    <span class="n">stream_function_name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">stream_function</span><span class="o">.</span><span class="vm">__name__</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">stream_function</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="s1">''</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_model_name</span> <span class="o">=</span> <span class="n">model_name</span> <span class="ow">or</span> <span class="sa">f</span><span class="s1">'function:</span><span class="si">{</span><span class="n">function_name</span><span class="si">}</span><span class="s1">:</span><span class="si">{</span><span class="n">stream_function_name</span><span class="si">}</span><span class="s1">'</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.function.FunctionModel.model_name" class="doc doc-heading">
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






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.function.FunctionModel.system" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">system</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code><span class="n">system</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The system / model provider.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.models.function.AgentInfo" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">AgentInfo</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>Information about an agent.</p>
<p>This is passed as the second to functions used within <a class="autorefs autorefs-internal" href="#pydantic_ai.models.function.FunctionModel"><code>FunctionModel</code></a>.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/function.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">148</span>
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
<span class="normal">166</span></pre></div></td><td class="code"><div><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code tabindex="0"><span class="nd">@dataclass</span><span class="p">(</span><span class="n">frozen</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="k">class</span><span class="w"> </span><span class="nc">AgentInfo</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Information about an agent.</span>

<span class="sd">    This is passed as the second to functions used within [`FunctionModel`][pydantic_ai.models.function.FunctionModel].</span>
<span class="sd">    """</span>

    <span class="n">function_tools</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ToolDefinition</span><span class="p">]</span>
<span class="w">    </span><span class="sd">"""The function tools available on this agent.</span>

<span class="sd">    These are the tools registered via the [`tool`][pydantic_ai.Agent.tool] and</span>
<span class="sd">    [`tool_plain`][pydantic_ai.Agent.tool_plain] decorators.</span>
<span class="sd">    """</span>
    <span class="n">allow_text_result</span><span class="p">:</span> <span class="nb">bool</span>
<span class="w">    </span><span class="sd">"""Whether a plain text result is allowed."""</span>
    <span class="n">result_tools</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ToolDefinition</span><span class="p">]</span>
<span class="w">    </span><span class="sd">"""The tools that can called as the final result of the run."""</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""The model settings passed to the run call."""</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.function.AgentInfo.function_tools" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">function_tools</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code><span class="n">function_tools</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolDefinition" href="../../tools/#pydantic_ai.tools.ToolDefinition">ToolDefinition</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The function tools available on this agent.</p>
<p>These are the tools registered via the <a class="autorefs autorefs-internal" href="../../agent/#pydantic_ai.agent.Agent.tool"><code>tool</code></a> and
<a class="autorefs autorefs-internal" href="../../agent/#pydantic_ai.agent.Agent.tool_plain"><code>tool_plain</code></a> decorators.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.function.AgentInfo.allow_text_result" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">allow_text_result</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_11"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_11 > code"></button><code><span class="n">allow_text_result</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Whether a plain text result is allowed.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.function.AgentInfo.result_tools" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">result_tools</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code><span class="n">result_tools</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolDefinition" href="../../tools/#pydantic_ai.tools.ToolDefinition">ToolDefinition</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The tools that can called as the final result of the run.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.function.AgentInfo.model_settings" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">model_settings</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_13"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_13 > code"></button><code><span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The model settings passed to the run call.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.models.function.DeltaToolCall" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">DeltaToolCall</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>Incremental change to a tool call.</p>
<p>Used to describe a chunk when streaming structured responses.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/function.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">169</span>
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
<span class="normal">181</span></pre></div></td><td class="code"><div><pre id="__code_14"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_14 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">DeltaToolCall</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Incremental change to a tool call.</span>

<span class="sd">    Used to describe a chunk when streaming structured responses.</span>
<span class="sd">    """</span>

    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""Incremental change to the name of the tool."""</span>
    <span class="n">json_args</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""Incremental change to the arguments as JSON"""</span>
    <span class="n">tool_call_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""Incremental change to the tool call ID."""</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.function.DeltaToolCall.name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_15"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_15 > code"></button><code><span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Incremental change to the name of the tool.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.function.DeltaToolCall.json_args" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">json_args</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_16"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_16 > code"></button><code><span class="n">json_args</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Incremental change to the arguments as JSON</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.function.DeltaToolCall.tool_call_id" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">tool_call_id</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_17"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_17 > code"></button><code><span class="n">tool_call_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Incremental change to the tool call ID.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.models.function.DeltaToolCalls" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">DeltaToolCalls</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_18"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_18 > code"></button><code><span class="n">DeltaToolCalls</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.TypeAlias" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypeAlias">TypeAlias</a></span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.function.DeltaToolCall" href="#pydantic_ai.models.function.DeltaToolCall">DeltaToolCall</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>A mapping of tool call IDs to incremental changes.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.models.function.FunctionDef" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">FunctionDef</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_19"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_19 > code"></button><code><span class="n">FunctionDef</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.TypeAlias" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypeAlias">TypeAlias</a></span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[</span>
    <span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.function.AgentInfo" href="#pydantic_ai.models.function.AgentInfo">AgentInfo</a></span><span class="p">],</span>
    <span class="n"><a class="autorefs autorefs-external" title="typing.Union" href="https://docs.python.org/3/library/typing.html#typing.Union">Union</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponse" href="../../messages/#pydantic_ai.messages.ModelResponse">ModelResponse</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponse" href="../../messages/#pydantic_ai.messages.ModelResponse">ModelResponse</a></span><span class="p">]],</span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>A function used to generate a non-streamed response.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.models.function.StreamFunctionDef" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">StreamFunctionDef</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_20"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_20 > code"></button><code><span class="n">StreamFunctionDef</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.TypeAlias" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypeAlias">TypeAlias</a></span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[</span>
    <span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.function.AgentInfo" href="#pydantic_ai.models.function.AgentInfo">AgentInfo</a></span><span class="p">],</span>
    <span class="n"><a class="autorefs autorefs-external" title="collections.abc.AsyncIterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator">AsyncIterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="typing.Union" href="https://docs.python.org/3/library/typing.html#typing.Union">Union</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.function.DeltaToolCalls" href="#pydantic_ai.models.function.DeltaToolCalls">DeltaToolCalls</a></span><span class="p">]],</span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>A function used to generate a streamed response.</p>
<p>While this is defined as having return type of <code>AsyncIterator[Union[str, DeltaToolCalls]]</code>, it should
really be considered as <code>Union[AsyncIterator[str], AsyncIterator[DeltaToolCalls]</code>,</p>
<p>E.g. you need to yield all text or all <code>DeltaToolCalls</code>, not mix them.</p>
    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.models.function.FunctionStreamedResponse" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">FunctionStreamedResponse</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_ai.models.StreamedResponse" href="../base/#pydantic_ai.models.StreamedResponse">StreamedResponse</a></code></p>


        <p>Implementation of <code>StreamedResponse</code> for <a class="autorefs autorefs-internal" href="#pydantic_ai.models.function.FunctionModel">FunctionModel</a>.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/function.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">202</span>
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
<span class="normal">242</span></pre></div></td><td class="code"><div><pre id="__code_21"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_21 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">FunctionStreamedResponse</span><span class="p">(</span><span class="n">StreamedResponse</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Implementation of `StreamedResponse` for [FunctionModel][pydantic_ai.models.function.FunctionModel]."""</span>

    <span class="n">_model_name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">_iter</span><span class="p">:</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="nb">str</span> <span class="o">|</span> <span class="n">DeltaToolCalls</span><span class="p">]</span>
    <span class="n">_timestamp</span><span class="p">:</span> <span class="n">datetime</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="n">_utils</span><span class="o">.</span><span class="n">now_utc</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">__post_init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_usage</span> <span class="o">+=</span> <span class="n">_estimate_usage</span><span class="p">([])</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_get_event_iterator</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">ModelResponseStreamEvent</span><span class="p">]:</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_iter</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
                <span class="n">response_tokens</span> <span class="o">=</span> <span class="n">_estimate_string_tokens</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_usage</span> <span class="o">+=</span> <span class="n">usage</span><span class="o">.</span><span class="n">Usage</span><span class="p">(</span><span class="n">response_tokens</span><span class="o">=</span><span class="n">response_tokens</span><span class="p">,</span> <span class="n">total_tokens</span><span class="o">=</span><span class="n">response_tokens</span><span class="p">)</span>
                <span class="k">yield</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parts_manager</span><span class="o">.</span><span class="n">handle_text_delta</span><span class="p">(</span><span class="n">vendor_part_id</span><span class="o">=</span><span class="s1">'content'</span><span class="p">,</span> <span class="n">content</span><span class="o">=</span><span class="n">item</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">delta_tool_calls</span> <span class="o">=</span> <span class="n">item</span>
                <span class="k">for</span> <span class="n">dtc_index</span><span class="p">,</span> <span class="n">delta_tool_call</span> <span class="ow">in</span> <span class="n">delta_tool_calls</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                    <span class="k">if</span> <span class="n">delta_tool_call</span><span class="o">.</span><span class="n">json_args</span><span class="p">:</span>
                        <span class="n">response_tokens</span> <span class="o">=</span> <span class="n">_estimate_string_tokens</span><span class="p">(</span><span class="n">delta_tool_call</span><span class="o">.</span><span class="n">json_args</span><span class="p">)</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">_usage</span> <span class="o">+=</span> <span class="n">usage</span><span class="o">.</span><span class="n">Usage</span><span class="p">(</span><span class="n">response_tokens</span><span class="o">=</span><span class="n">response_tokens</span><span class="p">,</span> <span class="n">total_tokens</span><span class="o">=</span><span class="n">response_tokens</span><span class="p">)</span>
                    <span class="n">maybe_event</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parts_manager</span><span class="o">.</span><span class="n">handle_tool_call_delta</span><span class="p">(</span>
                        <span class="n">vendor_part_id</span><span class="o">=</span><span class="n">dtc_index</span><span class="p">,</span>
                        <span class="n">tool_name</span><span class="o">=</span><span class="n">delta_tool_call</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
                        <span class="n">args</span><span class="o">=</span><span class="n">delta_tool_call</span><span class="o">.</span><span class="n">json_args</span><span class="p">,</span>
                        <span class="n">tool_call_id</span><span class="o">=</span><span class="n">delta_tool_call</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">,</span>
                    <span class="p">)</span>
                    <span class="k">if</span> <span class="n">maybe_event</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                        <span class="k">yield</span> <span class="n">maybe_event</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">model_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the model name of the response."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_model_name</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">timestamp</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">datetime</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the timestamp of the response."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_timestamp</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.function.FunctionStreamedResponse.model_name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">model_name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_22"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_22 > code"></button><code><span class="n">model_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Get the model name of the response.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.function.FunctionStreamedResponse.timestamp" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">timestamp</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_23"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_23 > code"></button><code><span class="n">timestamp</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="datetime.datetime" href="https://docs.python.org/3/library/datetime.html#datetime.datetime">datetime</a></span>
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